import logging
from typing import TYPE_CHECKING
import json

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

logger = logging.getLogger("Client")

from . import levels
#call levels data as levels.database
from .items import ITEM_NAME_TO_ID

password_selector_addresses = [ 0x0502, 0x0503, 0x0504, 0x0505, 0x0506 ]

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

class BubbleBobbleClient(BizHawkClient):
    game = "Bubble Bobble"
    system = "NES"

    def __init__(self):
        super().__init__()

    def compile_ids(self, ctx: "BizHawkClientContext"):
        self.ids_received = []
        for items in ctx.items_received:
            self.ids_received.append(int(items[0]))

    def levelcheck(self, ctx: "BizHawkClientContext", level: int, purpose):
        #purpose is 0 for checking levels for active gameplay or 1 for returning a valid password
        check = level - 1
        passwords = levels.database[check].passwords + levels.database[check].supers #once I figure out how to differentiate super levels, this part needs adjusting
        for password in passwords:
            has_letter = []
            for letter in password:
                if ITEM_NAME_TO_ID[letter] in self.ids_received:
                    has_letter.append(letter)
                    if len(has_letter) == 5 and purpose == 0:
                        return True
                    if len(has_letter) == 5 and purpose == 1:
                        return has_letter
        return False
    
    async def checkstartinglives(self, ctx: "BizHawkClientContext"):
        self.starting_lives_should_be = self.ids_received.count(2) + 3
        current_starting_lives = await bizhawk.read(ctx.bizhawk_ctx,[(0xCA38, 1, "System Bus")])
        if self.starting_lives_should_be != current_starting_lives: await bizhawk.write(ctx.bizhawk_ctx, [(0x0042, extra_starting_lives.to_bytes(1), "RAM")])

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        rom_hash = await bizhawk.get_hash(ctx.bizhawk_ctx)
        rom_system = await bizhawk.get_system(ctx.bizhawk_ctx)
        if rom_hash == "B220CB06A7E23C55A982FD75B32554D0BF511B7B" and rom_system == "NES":
            ctx.game = self.game
            ctx.items_handling = 0b111
            ctx.want_slot_data = True
            ctx.watcher_timeout = 0.1
            return True
        else: return False

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        self.compile_ids(ctx)
        if cmd == "Connected":
            slotdata = args['slot_data']
            self.separate_supers = bool(slotdata['separate_super_bubble_bobble_levels'])
            self.lock_supers = bool(slotdata['lock_super_bubble_bobble_levels'])
            self.lock_2p = bool(slotdata['lock_two_player_mode'])
            self.require_best = bool(slotdata['require_best_ending'])
            if 2 in self.ids_received: checkstartinglives()

        if cmd == "ReceivedItems":
            check_received = []
            for x in args['items']:
                check_received.append(x['item'])
            if 2 in check_received: checkstartinglives()

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:

#reminder: the command for sending text to the client is logger.info()

        try:
            self.previous_enemy_count = self.current_enemy_count
        except:
            self.previous_enemy_count = 0
            
#REMEMBER THAT THIS IS A LIST OF BYTES
        read_data = await bizhawk.read(ctx.bizhawk_ctx,[(0x0401, 1, "RAM"), (0x002E, 1, "RAM"), (0x0042, 1, "RAM"), (0x0496, 1, "RAM"), (0x0502, 1, "RAM"), (0x0503, 1, "RAM"), (0x0504, 1, "RAM"), (0x0505, 1, "RAM"), (0x0506, 1, "RAM"), (0x0402, 1, "RAM"), (0x050A, 1, "RAM")])
        current_level = int.from_bytes(read_data[0])
        p1_lives = int.from_bytes(read_data[1])
        p2_lives = int.from_bytes(read_data[2])
        self.current_enemy_count = int.from_bytes(read_data[3])
        current_menu_selection = int.from_bytes(read_data[9])
        current_letter_position = int.from_bytes(read_data[10])

        if current_level > 0 and (p1_lives > 0 or p2_lives > 0):
            check = self.levelcheck(ctx, current_level, 0)
            #once I figure out how to check for boss fights, run self.levelcheck() for both 99 and B2
            if check and self.previous_enemy_count > 0:
                if self.lock_2p and 8 not in self.ids_received and p2_lives > 0:
                    await bizhawk.write(ctx.bizhawk_ctx, [(0x0042, b'\x00', "RAM")])
                if self.current_enemy_count == 0:
                    level_id = current_level + 1000
                    #if supers are separate, and a super level was beaten, add another 1000
                    level_id = [level_id]
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": level_id
                    }])
                #else: check for timer traps here
            elif not check and self.current_enemy_count > 0: await bizhawk.write(ctx.bizhawk_ctx, [(0x002E, b'\x00', "RAM"), (0x0042, b'\x00', "RAM"), (0x0401, b'\x00', "RAM")])

        elif current_menu_selection == 4:
            try:
                self.previous_password_int = self.selected_password_int
            except:
                self.previous_password_int = [-1, -1, -1, -1, -1]
            selected_password_bytes = read_data[4:9]
            self.selected_password_int = []
            for letter in selected_password_bytes:
                self.selected_password_int.append(int.from_bytes(letter))
            check_selected_letter_id = ((current_letter_position - 1) * 10) + self.selected_password_int[current_letter_position]
            while check_selected_letter_id not in self.ids_received:
                if self.selected_password_int[id] > self.previous_password_int[id]:
                    check_selected_letter_id += 1
                    if check_selected_letter_id % 10 == 0: check_selected_letter_id -= 10
                elif self.selected_password_int[id] < self.previous_password_int[id]:
                    check_selected_letter_id -= 1
                    if check_selected_letter_id % 10 == 9: check_selected_letter_id += 10
                while check_selected_letter_id >= 10: check_selected_letter_id -= 10
                await bizhawk.write(ctx.bizhawk_ctx, [(password_selector_addresses[current_letter_position], check_selected_letter_id.to_bytes(1), "RAM")])

"""
define a self.timer_traps_applied to keep track of how many timer traps have been received and used
network protocol document explains how to save this on the server if needed

start by reading all the stuff needed to check everything below all at once
if the player is on the title screen: just wait
if the player is on the main menu: monitor what the player attempts to input as a password and change it if they use a letter they're not supposed to use
if the player is in game:
    if the player is in a regular level:
        first check if they are allowed to be in that level at all and kill both player one and player two if they're not
            including if it's a Super level, depending on whether supers are locked
        second check if two player mode is turned on and force player two's lives to 0 if it's not
        third disable/enable skills/elements based on collected items
        fourth watch for level completion and send a check when the level is completed
        last check if any timer traps have been received and apply them if applicable
            compare number of traps received to number of traps applied
            verify that monster count and timer are above 0
    if the player is in the boss fight:
        check if the player is allowed to go to level 99 or B2 and kill them if they're not
        monitor for completion
        check if they're getting the good ending or a bad ending and send completion accordingly
"""