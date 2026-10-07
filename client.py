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
from .rom import PlayerNameAddress, APidentifierAddress

password_selector_addresses = [ 0x0502, 0x0503, 0x0504, 0x0505, 0x0506 ]

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor

@mark_raw
def cmd_find_password(self: 'BizHawkClientCommandProcessor', checklevel: str = ""):
    """Locates an available valid password for a level."""
    ctx = self.ctx
    client = ctx.client_handler
    separate = client.separate_supers | client.lock_supers
    try:
        for x in range(len(levels.database)):
            text = checklevel.title()
            if text == levels.database[x].lev:
                check = x + 1
                superlevel = False
                break
            if text == levels.database[x].sup:
                check = x + 1
                superlevel = True
                break
        passwords_list = levelcheck(client.ids_received, check, 1, superlevel, separate)
        newlist = []
        for y in passwords_list:
            newlist.append(y.strip("- "))
        logger.info(f'Try password {" ".join(newlist)} for {text}.')
    except:
        logger.info('Invalid or unavailable level')

def cmd_toggle_deathlink(self: 'BizHawkClientCommandProcessor'):
    """Toggles death link."""
    ctx = self.ctx
    client = ctx.client_handler
    if client.deathlink:
        client.deathlink = False
        logger.info('Deathlink disabled')
    else:
        client.deathlink = True
        logger.info('Deathlink enabled')

def levelcheck(ids: list, level: int, purpose: int, superlevel: bool, separate: bool):
    #purpose is 0 for checking levels for active gameplay or 1 for returning a valid password

    check = level - 1
    if separate:
        if superlevel: passwords = levels.database[check].supers
        else: passwords = levels.database[check].passwords
    else: passwords = levels.database[check].supers + levels.database[check].passwords
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
    patch_suffix = ".apbubbob"

    def __init__(self):
        super().__init__()

    def compile_ids(self, ctx: "BizHawkClientContext"):
        self.ids_received = []
        for items in ctx.items_received:
            self.ids_received.append(int(items[0]))

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        rom_system = await bizhawk.get_system(ctx.bizhawk_ctx)
        rom_identifier = await bizhawk.read(ctx.bizhawk_ctx,[(APidentifierAddress - 0x10, 0x8, "PRG ROM")])
        rom_identifier = rom_identifier[0]
        rom_identifier = rom_identifier.decode("ascii")
        rom_player_name = await bizhawk.read(ctx.bizhawk_ctx,[(PlayerNameAddress - 0x10, 0x20, "PRG ROM")])
        rom_player_name = bytes([byte for byte in rom_player_name[0] if byte != 0]).decode("ascii")
        self.rom_slot_name = rom_player_name

        try:
            if rom_system == "NES" and rom_identifier == "BUBBOBAP":
                await bizhawk.write(ctx.bizhawk_ctx, [(0x0402, b'\x00', "RAM")])
                ctx.game = self.game
                ctx.items_handling = 0b111
                ctx.want_slot_data = True
                ctx.watcher_timeout = 0.1
                logger.info('-')
                logger.info('Use \'/find_level Level ##\' or \'/find_level Super ##\' to identify a valid password for a level.')
                logger.info('-')
                ctx.command_processor.commands["find_password"] = cmd_find_password
                ctx.command_processor.commands["find_level"] = cmd_find_password
                ctx.command_processor.commands["toggle_deathlink"] = cmd_toggle_deathlink
                self.initialize = True
                return True
            else: return False
        except: return False

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        ctx.auth = self.rom_slot_name

    def on_package(self, ctx: "BizHawkClientContext", cmd: str, args: dict) -> None:
        
        if cmd == "Connected":
            slotdata = args['slot_data']
            self.separate_supers = bool(slotdata['separate_super_bubble_bobble_levels'])
            self.lock_supers = bool(slotdata['lock_super_bubble_bobble_levels'])
            self.lock_2p = bool(slotdata['lock_two_player_mode'])
            self.require_best = bool(slotdata['require_best_ending'])
            self.deathlink = bool(slotdata['deathlink'])
            self.deathlinktrigger = bool(slotdata['deathlinktrigger'])
            self.deathlinkresult = bool(slotdata['deathlinkresult'])
            self.slot = args["slot"]

        if cmd == "Retrieved":
            if "bubbobtraps_applied" in args["keys"]:
                if args["keys"]["bubbobtraps_applied"] == None:
                    self.traps_applied = 0
                else: self.traps_applied = args["keys"]["bubbobtraps_applied"][str(self.slot)]

        if cmd == "Bounced" and self.deathlink and "DeathLink" in args["tags"] and args["data"]["source"] != ctx.slot_info[ctx.slot].name: self.death_received = True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:

        self.compile_ids(ctx)
        self.traps_received = self.ids_received.count(1)
        self.writes = []
        self.kill_p1 = False
        self.kill_p2 = False
        self.reset_level = False

        try:
            self.previous_enemy_count = self.current_enemy_count
        except:
            self.previous_enemy_count = 0

        try:
            self.previous_level = self.current_level
        except:
            self.previous_level = 0
            
        #REMEMBER THAT THIS IS A LIST OF BYTES
        read_data = await bizhawk.read(ctx.bizhawk_ctx,[(0x0401, 1, "RAM"), (0x002E, 1, "RAM"), (0x0042, 1, "RAM"), (0x0496, 1, "RAM"), (0x0502, 1, "RAM"), (0x0503, 1, "RAM"), (0x0504, 1, "RAM"), (0x0505, 1, "RAM"), (0x0506, 1, "RAM"), (0x0402, 1, "RAM"), (0x050A, 1, "RAM"), (0x040D, 1, "RAM"), (0x0031, 1, "RAM"), (0x0084, 1, "RAM"), (0x046C, 1, "RAM"), (0x0327, 1, "RAM"), (0x032C, 1, "RAM"), (0x006F, 1, "RAM"), (0x0400, 1, "RAM"), (0x04CE, 1, "RAM"), (0x0038, 6, "RAM"), (0x01D3, 1, "RAM"), (0x00DC, 1, "RAM"), (0x0045, 1, "RAM"), (0x0030, 1, "RAM")])

        self.current_level = int.from_bytes(read_data[0])
        p1_lives = int.from_bytes(read_data[1])
        p2_lives = int.from_bytes(read_data[2])
        self.current_enemy_count = int.from_bytes(read_data[3])
        current_menu_selection = int.from_bytes(read_data[9])
        current_letter_position = int.from_bytes(read_data[10])
        current_timer = int.from_bytes(read_data[11])
        game_state = int.from_bytes(read_data[13])
        score_check = int.from_bytes(read_data[20])
        last_level_beaten = int.from_bytes(read_data[21])
        completion_check = int.from_bytes(read_data[22])

        #this part hopefully identifies super levels
        self.super_check_1 = int.from_bytes(read_data[14])
        if self.super_check_1 >= 1: self.super_level = True
        else: self.super_level = False

        #this hopefully checks for boss fights
        self.boss_check_1 = int.from_bytes(read_data[15])
        self.boss_check_2 = int.from_bytes(read_data[16])
        self.boss_hp = int.from_bytes(read_data[17])
        if self.boss_check_1 == 102 and self.boss_check_2 == 4 and (self.current_level == 99 or self.current_level >= 112): self.boss_fight = True
        else: self.boss_fight = False
        
        self.transition = int.from_bytes(read_data[18])
        #this is set to 2 for level transitions

        if self.current_level == 0:
            if p1_lives == 0 and p2_lives == 0: self.previous_level = 0
            else: self.current_level = self.previous_level
        level_difference = self.current_level - self.previous_level
        if level_difference < 0: self.current_level = self.previous_level

        #this hopefully sets starting lives
        self.starting_lives_should_be = self.ids_received.count(2) + 3
        self.writes.append((0x01D0, self.starting_lives_should_be.to_bytes(1), "RAM"))

        #UNLEASH DEAHTLINK
        if self.deathlink:
            self.player1_state = int.from_bytes(read_data[12])
            self.player2_state = int.from_bytes(read_data[23])
            if self.player1_state != 128: self.player1_dying = False
            if self.player2_state != 128: self.player2_dying = False
            if self.player1_state == 128 and self.player1_dying == False:
                self.player1_dying = True
                if self.deathlinktrigger: await ctx.send_death("Bub\'s bubble popped.")
                elif p1_lives == 1 and (p2_lives == 0 or (p2_lives == 1 and self.player2_state == 128)): await ctx.send_death("Bub ran out of lives.")
            if self.player2_state == 128 and self.player2_dying == False:
                self.player2_dying = True
                if self.deathlinktrigger: await ctx.send_death("Bob\'s bubble popped.")
                elif p2_lives == 1 and (p1_lives == 0 or (p1_lives == 1 and self.player1_state == 128)): await ctx.send_death("Bob ran out of lives.")
            try:
                if self.death_received:
                    self.death_received = False
                    if self.deathlinkresult:
                        self.kill_p1 = True
                        self.kill_p2 = True
                        self.reset_level = True
                    else:
                        self.player1_dying = True
                        self.player2_dying = True
                        if p1_lives > 0: self.writes.append((0x0031, b'\x80', "RAM"))
                        if p2_lives > 0: self.writes.append((0x0045, b'\x80', "RAM"))
            except: self.death_received = False

        #this part checks for level completion and sends a check hopefully
        if last_level_beaten > 0 and score_check > 0 and (self.transition == 2 or self.boss_fight):
            last_level_beaten += 1000
            if self.separate_supers and self.super_level: last_level_beaten += 1000
            try:
                if last_level_beaten not in self.locations_sent:
                    last_level_beaten = [last_level_beaten]
                    await ctx.send_msgs([{
                        "cmd": "LocationChecks",
                        "locations": last_level_beaten
                    }])
                    self.locations_sent.append(last_level_beaten)
            except: self.locations_sent = []

        if game_state == 255:
            self.previous_level = 0
            self.current_level = 0

        #hopefully this checks and sends completion
        if completion_check == 4 or completion_check == 32 or completion_check == 31 or (completion_check == 29 and not self.require_best):
            await ctx.send_msgs([{
                "cmd": "StatusUpdate",
                "status": ClientStatus.CLIENT_GOAL
            }])

        if self.current_level > 0 and (p1_lives > 0 or p2_lives > 0):
            separate = self.separate_supers | self.lock_supers
            if self.boss_fight:
                check99 = levelcheck(self.ids_received, 99, 0, self.super_level, separate)
                checkB2 = levelcheck(self.ids_received, 112, 0, self.super_level, separate)
                check = check99 | checkB2
                if 5 not in self.ids_received:
                    if self.boss_hp < 55: self.writes.append((0x006F, b'\x3c', "RAM"))
            else: check = levelcheck(self.ids_received, self.current_level, 0, self.super_level, separate)

            if check:

                #this part kills player 2 if 2 player mode is supposed to be locked
                if self.lock_2p and 8 not in self.ids_received and p2_lives > 0: self.kill_p2 = True

                #this part hopefully kills you if you're in a super level and not supposed to be
                if self.super_level and self.lock_supers and 9 not in self.ids_received: 
                    self.kill_p1 = True
                    self.kill_p2 = True
                    self.reset_level = True

                #this part checks for traps
                elif self.current_enemy_count > 0 and not self.boss_fight:
                    try:
                        if current_timer >= 2 and self.traps_applied < self.traps_received:
                            self.writes.append((0x040D, b'\x00', "RAM"))
                            self.traps_applied += 1
                            await ctx.send_msgs([{
                                "cmd": "Set",
                                "key": "bubbobtraps_applied",
                                "default": {self.slot : 0},
                                "want_reply": False,
                                "operations": [{"operation": "replace", "value": {self.slot : self.traps_applied}}]
                            }])
                    except: await ctx.send_msgs([{"cmd": "Get", "keys": ["bubbobtraps_applied"]}])

            #this part kills you if you're in a level that you're not supposed to be in
            elif not check: 
                self.kill_p1 = True
                self.kill_p2 = True
                self.reset_level = True

        #this part changes the current selected letter if you have a letter selected that you're not allowed to use yet
        elif current_menu_selection == 4 and current_letter_position < 5:
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
                    self.writes.append((password_address, [check_selected_letter_id], "RAM"))
            except: self.compile_ids(ctx)

        self.current_elements = int.from_bytes(read_data[19])
        self.elements_unlocked = 17
        if 6 in self.ids_received: self.elements_unlocked += 34
        if 4 in self.ids_received: self.elements_unlocked += 68
        if 5 in self.ids_received: self.elements_unlocked += 136
        self.current_elements &= self.elements_unlocked
        self.writes.append((0x04CE, self.current_elements.to_bytes(1), "RAM"))

        self.current_powerups = int.from_bytes(read_data[24])
        self.powerups_unlocked = 56
        if not self.boss_fight:
            if 61 in self.ids_received: self.powerups_unlocked += 1
            if 62 in self.ids_received: self.powerups_unlocked += 2
            if 63 in self.ids_received: self.powerups_unlocked += 4
        elif 7 in self.ids_received: self.powerups_unlocked += 71
        self.current_powerups &= self.powerups_unlocked
        self.writes.append((0x0030, self.current_powerups.to_bytes(1), "RAM"))

        if 3 in self.ids_received: self.writes.append((0x01D1, b'\x01', "RAM"))
        else: self.writes.append((0x01D1, b'\x00', "RAM"))
        
        if self.kill_p1: self.writes.append((0x002E, b'\x00', "RAM"))
        if self.kill_p2: self.writes.append((0x0042, b'\x00', "RAM"))
        if self.reset_level: self.writes.append((0x0401, b'\x00', "RAM"))

        await bizhawk.write(ctx.bizhawk_ctx, self.writes)