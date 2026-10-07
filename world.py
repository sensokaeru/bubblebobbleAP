from collections.abc import Mapping
from typing import Any, ClassVar

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as bubblebobble_options

from . import rom
import os
import Utils
import settings

class BubbleBobbleSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Bubble Bobble US ROM"""
        copy_to = "Bubble Bobble (USA).nes"
        description = "Bubble Bobble (USA) ROM file"
        md5s = rom.BubBobHash
    
    rom_file: RomFile = RomFile(RomFile.copy_to)

class BubbleBobbleWorld(World):
    """
    Bubble Bobble for AP is the NES classic with progression locked behind the password
    system, only allowing the player to go to a level if they have the letters required
    for one of its passwords.
    """

    game = "Bubble Bobble"

    web = web_world.BubbleBobbleWebWorld()

    options_dataclass = bubblebobble_options.BubbleBobbleOptions
    options: bubblebobble_options.BubbleBobbleOptions
    settings: ClassVar[BubbleBobbleSettings]
    settings_key = "bubble_bobble_settings"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Bubble Bobble"
    
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BubbleBobbleItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict("separate_super_bubble_bobble_levels", "lock_super_bubble_bobble_levels", "lock_two_player_mode", "require_best_ending", "deathlink", "deathlinktrigger", "deathlinkresult")

    def generate_output(self, output_directory: str):
        outfilepname = f"_P{self.player}"
        outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
        self.rom_name_text = f'BUB{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}\0'
        self.romName = bytearray(self.rom_name_text, "utf8")[:0x20]
        self.romName.extend([0] * (0x20 - len(self.romName)))
        self.rom_name = self.romName
        self.playerName = bytearray(self.multiworld.player_name[self.player], "utf8")[:0x20]
        self.playerName.extend([0] * (0x20 - len(self.playerName)))
        patch = rom.BubbleBobbleProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        procedure = [("apply_tokens", ["token_data.bin"])]
        patch.procedure = procedure
        rom.write_tokens(self, patch)
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))

