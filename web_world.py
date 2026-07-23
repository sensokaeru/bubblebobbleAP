from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class BubbleBobbleWebWorld(WebWorld):
    game = "Bubble Bobble"
    theme = "grassFlowers"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Bubble Bobble for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Sensokaeru"],
    )
    tutorials = [setup_en]
    option_groups = option_groups
    options_presets = option_presets