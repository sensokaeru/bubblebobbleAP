from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as bubblebobble_options

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
        pass
        #fill in slot data eventually, below is APQuest's example
    #    return self.options.as_dict(
    #        "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
    #    )