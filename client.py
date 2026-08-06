import logging
from typing import TYPE_CHECKING
import json

from NetUtils import ClientStatus
from MultiServer import mark_raw

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

logger = logging.getLogger("Client")

from . import levels
#call levels data as levels.database
from .items import ITEM_NAME_TO_ID

password_selector_addresses = [ 0x0502, 0x0503, 0x0504, 0x0505, 0x0506 ]

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor

@mark_raw
def cmd_find_password(self: 'BizHawkClientCommandProcessor', checklevel: str = ""):
    """Locates an available valid password for a level."""
    ctx = self.ctx
    client = ctx.client_handler
    try:
        for x in range(len(levels.database)):
            text = checklevel.title()
            if text == levels.database[x].lev or text == levels.database[x].sup:
                check = x + 1
                break
        passwords_list = levelcheck(client.ids_received, check, 1)
        newlist = []
        for y in passwords_list:
            newlist.append(y.strip("- "))
        logger.info(f'Try password {" ".join(newlist)} for {text}.')
    except:
        logger.info('Invalid or unavailable level')

def levelcheck(ids: list, level: int, purpose: int):
    #purpose is 0 for checking levels for active gameplay or 1 for returning a valid password
    #once I figure out how to differentiate super levels, this part needs adjusting

    check = level - 1
    passwords = levels.database[check].passwords + levels.database[check].supers
    for password in passwords:
        has_letter = []
        for letter in password:
            if ITEM_NAME_TO_ID[letter] in ids:
                has_letter.append(letter)
                if len(has_letter) == 5 and purpose == 0:
                    return True
                if len(has_letter) == 5 and purpose == 1:
                    return has_letter
    return False

class BubbleBobbleClient(BizHawkClient):
    game = "Bubble Bobble"
    system = "NES"

    def __init__(self):
        super().__init__()

    def compile_ids(self, ctx: "BizHawkClientContext"):
        self.ids_received = []
        for items in ctx.items_received:
            self.ids_received.append(int(items[0]))

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        rom_hash = await bizhawk.get_hash(ctx.bizhawk_ctx)
        rom_system = await bizhawk.get_system(ctx.bizhawk_ctx)
        if rom_hash == "B220CB06A7E23C55A982FD75B32554D0BF511B7B" and rom_system == "NES":
            await bizhawk.write(ctx.bizhawk_ctx, [(0x0402, b'\x00', "RAM")])
            ctx.game = self.game
            ctx.items_handling = 0b111
            ctx.want_slot_data = True
            ctx.watcher_timeout = 0.15
            logger.info('-')
            logger.info('Use \'/find_level Level ##\' or \'/find_level Super ##\' to identify a valid password for a level.')
            logger.info('-')
            ctx.command_processor.commands["find_password"] = cmd_find_password
            ctx.command_processor.commands["find_level"] = cmd_find_password
            return True
        else: return False

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        self.compile_ids(ctx)
        self.traps_received = self.ids_received.count(1)
        if cmd == "Connected":
            slotdata = args['slot_data']
            self.separate_supers = bool(slotdata['separate_super_bubble_bobble_levels'])
            self.lock_supers = bool(slotdata['lock_super_bubble_bobble_levels'])
            self.lock_2p = bool(slotdata['lock_two_player_mode'])
            self.require_best = bool(slotdata['require_best_ending'])
            self.slot = args["slot"]

        if cmd == "Retrieved":
            if "bubbobtraps_applied" in args["keys"]:
                if args["keys"]["bubbobtraps_applied"] == None:
                    self.traps_applied = 0
                else: self.traps_applied = args["keys"]["bubbobtraps_applied"][str(self.slot)]

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        self.compile_ids(ctx)

        try:
            self.previous_enemy_count = self.current_enemy_count
        except:
            self.previous_enemy_count = 0

        try:
            self.previous_level = self.current_level
        except:
            self.previous_level = 0
            
#REMEMBER THAT THIS IS A LIST OF BYTES
        read_data = await bizhawk.read(ctx.bizhawk_ctx,[(0x0401, 1, "RAM"), (0x002E, 1, "RAM"), (0x0042, 1, "RAM"), (0x0496, 1, "RAM"), (0x0502, 1, "RAM"), (0x0503, 1, "RAM"), (0x0504, 1, "RAM"), (0x0505, 1, "RAM"), (0x0506, 1, "RAM"), (0x0402, 1, "RAM"), (0x050A, 1, "RAM"), (0x040D, 1, "RAM"), (0x0031, 1, "RAM"), (0x0084, 1, "RAM"), (0xCA38, 1, "System Bus")])

        self.current_level = int.from_bytes(read_data[0])
        if self.current_level == 0: self.previous_level = 0
        level_difference = self.current_level - self.previous_level
        if level_difference < 0: self.current_level = self.previous_level

        p1_lives = int.from_bytes(read_data[1])
        p2_lives = int.from_bytes(read_data[2])
        self.current_enemy_count = int.from_bytes(read_data[3])
        current_menu_selection = int.from_bytes(read_data[9])
        current_letter_position = int.from_bytes(read_data[10])
        current_timer = int.from_bytes(read_data[11])
        game_state = int.from_bytes(read_data[13])

        self.current_starting_lives = int.from_bytes(read_data[14])
        idsforthis = self.ids_received
        self.starting_lives_should_be = idsforthis.count(2) + 3
        if self.starting_lives_should_be != self.current_starting_lives:
            await bizhawk.write(ctx.bizhawk_ctx, [(0xCA38, self.starting_lives_should_be.to_bytes(1), "System Bus")])

        ####read_data[12] is going to be player state, watch it to implement death links, gets set to 128 or b'\x80' for death state

#trying again to check for level completion hope it fucking works this time
        if game_state == 128:
            checkprevious = levelcheck(self.ids_received, self.previous_level, 0)
            level_difference = self.current_level - self.previous_level
            if checkprevious and level_difference == 1:
                level_id = self.previous_level + 1000
                level_id = [level_id]
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": level_id
                }])

        elif game_state == 255:
            self.previous_level = 0
            self.current_level = 0

        if self.current_level > 0 and (p1_lives > 0 or p2_lives > 0):
            check = levelcheck(self.ids_received, self.current_level, 0)
            #once I figure out how to check for boss fights, run levelcheck() for both 99 and B2

            if check:
            #above line previously checked enemy count:  and self.previous_enemy_count > 0
                if self.lock_2p and 8 not in self.ids_received and p2_lives > 0: await bizhawk.write(ctx.bizhawk_ctx, [(0x0042, b'\x00', "RAM")])

#this part checks for traps
                elif self.current_enemy_count > 0:
                    try:
                        if current_timer >= 2 and self.traps_applied < self.traps_received:
                            await bizhawk.write(ctx.bizhawk_ctx, [(0x040D, b'\x00', "RAM")])
                            self.traps_applied += 1
                            await ctx.send_msgs([{
                                "cmd": "Set",
                                "key": "bubbobtraps_applied",
                                "default": {self.slot : 0},
                                "want_reply": False,
                                "operations": [{"operation": "replace", "value": {self.slot : self.traps_applied}}]
                            }])
                    except: await ctx.send_msgs([{"cmd": "Get", "keys": ["bubbobtraps_applied"]}])

#this part kills you if you're in a level that you're not supposed to be in.  This also previously compared enemy count, which might not be necessary : and self.current_enemy_count > 0
            elif not check: await bizhawk.write(ctx.bizhawk_ctx, [(0x002E, b'\x00', "RAM"), (0x0042, b'\x00', "RAM"), (0x0401, b'\x00', "RAM")])

#this part changes the current selected letter if you have a letter selected that you're not allowed to use yet
        elif current_menu_selection == 4:
            try:
                self.previous_password_int = self.selected_password_int
            except:
                self.previous_password_int = [-1, -1, -1, -1, -1]
            selected_password_bytes = read_data[4:9]
            self.selected_password_int = []
            for letter in selected_password_bytes:
                checkletter = int.from_bytes(letter)
                if checkletter > 9: checkletter = 0
                self.selected_password_int.append(checkletter)
            check_selected_letter_id = ((current_letter_position + 1) * 10) + self.selected_password_int[current_letter_position]
            try:
                if check_selected_letter_id not in self.ids_received:
                    if self.selected_password_int[current_letter_position] == self.previous_password_int[current_letter_position]: self.previous_password_int[current_letter_position] = -1
                    while check_selected_letter_id not in self.ids_received:
                        if self.selected_password_int[current_letter_position] > self.previous_password_int[current_letter_position]:
                            check_selected_letter_id += 1
                            if check_selected_letter_id % 10 == 0: check_selected_letter_id -= 10
                        elif self.selected_password_int[current_letter_position] < self.previous_password_int[current_letter_position]:
                            check_selected_letter_id -= 1
                            if check_selected_letter_id % 10 == 9: check_selected_letter_id += 10
                    while check_selected_letter_id >= 10: check_selected_letter_id -= 10
                    password_address = password_selector_addresses[current_letter_position]
                    write_response = await bizhawk.write(ctx.bizhawk_ctx, [(password_address, [check_selected_letter_id], "RAM")])
            except: self.compile_ids(ctx)

"""
(check)define a self.timer_traps_applied to keep track of how many timer traps have been received and used
(check)network protocol document explains how to save this on the server if needed

start by reading all the stuff needed to check everything below all at once
if the player is on the title screen: just wait
(check)if the player is on the main menu: monitor what the player attempts to input as a password and change it if they use a letter they're not supposed to use
if the player is in game:
    if the player is in a regular level:
        (check)first check if they are allowed to be in that level at all and kill both player one and player two if they're not
            including if it's a Super level, depending on whether supers are locked
        (check)second check if two player mode is turned on and force player two's lives to 0 if it's not
        third disable/enable skills/elements based on collected items
        (check)fourth watch for level completion and send a check when the level is completed
        last check if any timer traps have been received and apply them if applicable
            compare number of traps received to number of traps applied
            verify that monster count and timer are above 0
    if the player is in the boss fight:
        check if the player is allowed to go to level 99 or B2 and kill them if they're not
        monitor for completion
        check if they're getting the good ending or a bad ending and send completion accordingly
"""