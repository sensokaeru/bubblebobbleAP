import logging
from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from . import levels
#call levels data as levels.database

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

class BubbleBobbleClient(BizHawkClient):
    game = "Bubble Bobble"
    system = "NES"

    def __init__(self):
        super().__init__()

    def levelcheck(self, ctx: "BizHawkClientContext", level: int):
        check = level - 1
        passwords = levels.database[check].passwords + levels.database[check].supers
        for password in passwords:
            has_letter = 0
            for letter in password:
                if letter in ctx.items_received:
                    has_letter += 1
                    if has_letter == 5:
                        return true
        return false

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        rom_hash = await bizhawk.get_hash(ctx.bizhawk_ctx)
        rom_system = await bizhawk.get_system(ctx.bizhawk_ctx)
        if rom_hash == "B220CB06A7E23C55A982FD75B32554D0BF511B7B" and rom_system == "NES":
            ctx.game = self.game
            ctx.items_handling = 0b111
            ctx.want_slot_data = True
            ctx.watcher_timeout = 0.1
            return True
        else: return false

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        read_data = await bizhawk.read(ctx.bizhawk_ctx,[(0x0401, 1, "RAM")]) #REMEMBER THAT THIS IS A LIST OF BYTES
        current_level = int.from_bytes(read_data[0])
        if current_level > 0x00:
            if not self.levelcheck(ctx.bizhawk_ctx, current_level):
                await bizhawk.write(ctx.bizhawk_ctx, [(0x002E, 0, "RAM"), (0x0042, 0, "RAM")])

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