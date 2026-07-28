from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

class BubbleBobbleClient(BizHawkClient):
    game = "Bubble Bobble"
    system = "NES"

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            rom_hash = await bizhawk.get_has(ctx.bizhawk_ctx)
            rom_system = await bizhawk.get_system(ctx.bizhawk_ctx)
            if rom_hash != "B220CB06A7E23C55A982FD75B32554D0BF511B7B" or rom_system != "NES":
                return False
        except bizhawk.RequestFailedError:
            return False
        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True

        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        try:
            ######
            #this is where we start watching RAM