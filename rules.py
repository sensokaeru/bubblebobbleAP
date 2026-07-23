from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import BubbleBobbleWorld

level_and_rules_archive = [
    "Level 01" = {
        "req" : 0,
        "passwords" : [
            ["B - - - -","- B - - -","- - A - -","- - - A -","- - - - B"],
            ["B - - - -","- B - - -","- - A - -","- - - B -","- - - - I"],
            ["B - - - -","- B - - -","- - A - -","- - - F -","- - - - B"],
            ["B - - - -","- B - - -","- - A - -","- - - I -","- - - - G"],
            ["B - - - -","- B - - -","- - B - -","- - - A -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - B -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - F -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - I -","- - - - B"],
            ["B - - - -","- B - - -","- - D - -","- - - D -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - H -","- - - - D"],
            ["B - - - -","- B - - -","- - H - -","- - - H -","- - - - D"]
        ],
        "supers" : [
            ["B - - - -","- B - - -","- - A - -","- - - C -","- - - - B"],
            ["B - - - -","- B - - -","- - A - -","- - - D -","- - - - I"],
            ["B - - - -","- B - - -","- - A - -","- - - E -","- - - - B"],
            ["B - - - -","- B - - -","- - A - -","- - - H -","- - - - B"],
            ["B - - - -","- B - - -","- - A - -","- - - J -","- - - - I"],
            ["B - - - -","- B - - -","- - B - -","- - - C -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - D -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - E -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - G -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - H -","- - - - B"],
            ["B - - - -","- B - - -","- - B - -","- - - J -","- - - - B"],
            ["B - - - -","- B - - -","- - D - -","- - - A -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - B -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - C -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - E -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - F -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - G -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - I -","- - - - D"],
            ["B - - - -","- B - - -","- - D - -","- - - J -","- - - - D"],
            ["B - - - -","- B - - -","- - F - -","- - - D -","- - - - J"],
            ["B - - - -","- B - - -","- - F - -","- - - H -","- - - - I"],
            ["B - - - -","- B - - -","- - F - -","- - - J -","- - - - J"],
            ["B - - - -","- B - - -","- - H - -","- - - A -","- - - - D"],
            ["B - - - -","- B - - -","- - H - -","- - - C -","- - - - D"],
            ["B - - - -","- B - - -","- - H - -","- - - E -","- - - - D"],
            ["B - - - -","- B - - -","- - H - -","- - - F -","- - - - D"],
            ["B - - - -","- B - - -","- - I - -","- - - D -","- - - - I"],
            ["B - - - -","- B - - -","- - I - -","- - - H -","- - - - I"] 
        ]
    },
    "Level 02" = {
        "req" : 0,
        "passwords" : [
            ["B - - - -","- A - - -","- - A - -","- - - A -","- - - - B"],
            ["B - - - -","- A - - -","- - A - -","- - - B -","- - - - I"],
            ["B - - - -","- A - - -","- - A - -","- - - F -","- - - - B"],
            ["B - - - -","- A - - -","- - A - -","- - - I -","- - - - G"],
            ["B - - - -","- A - - -","- - H - -","- - - H -","- - - - D"] 
        ],
        "supers" : [
            ["B - - - -","- A - - -","- - A - -","- - - C -","- - - - B"],
            ["B - - - -","- A - - -","- - A - -","- - - D -","- - - - I"],
            ["B - - - -","- A - - -","- - A - -","- - - E -","- - - - B"],
            ["B - - - -","- A - - -","- - A - -","- - - H -","- - - - B"],
            ["B - - - -","- A - - -","- - A - -","- - - J -","- - - - I"],
            ["B - - - -","- A - - -","- - F - -","- - - D -","- - - - J"],
            ["B - - - -","- A - - -","- - F - -","- - - H -","- - - - I"],
            ["B - - - -","- A - - -","- - F - -","- - - J -","- - - - J"],
            ["B - - - -","- A - - -","- - H - -","- - - A -","- - - - D"],
            ["B - - - -","- A - - -","- - H - -","- - - C -","- - - - D"],
            ["B - - - -","- A - - -","- - H - -","- - - E -","- - - - D"],
            ["B - - - -","- A - - -","- - H - -","- - - F -","- - - - D"] 
        ]
    },
    "Level 03" = {
        "req" : "nothing",
        "passwords" : [
            ["B - - - -","- A - - -","- - B - -","- - - A -","- - - - I"],
            ["B - - - -","- A - - -","- - B - -","- - - B -","- - - - I"],
            ["B - - - -","- A - - -","- - B - -","- - - F -","- - - - G"],
            ["B - - - -","- A - - -","- - B - -","- - - I -","- - - - G"]
        ],
        "supers" : [
            ["B - - - -","- A - - -","- - B - -","- - - C -","- - - - I"],
            ["B - - - -","- A - - -","- - B - -","- - - D -","- - - - I"],
            ["B - - - -","- A - - -","- - B - -","- - - H -","- - - - I"],
            ["B - - - -","- A - - -","- - B - -","- - - J -","- - - - I"],
            ["B - - - -","- A - - -","- - I - -","- - - C -","- - - - J"],
            ["B - - - -","- A - - -","- - I - -","- - - D -","- - - - J"],
            ["B - - - -","- A - - -","- - I - -","- - - H -","- - - - J"],
            ["B - - - -","- A - - -","- - I - -","- - - J -","- - - - J"]
        ]
    },
    "Level 04" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 05" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 06" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 07" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 08" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 09" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 10" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 11" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 12" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 13" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 14" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 15" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 16" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 17" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 18" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 19" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 20" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 21" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 22" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 23" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 24" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 25" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 26" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 27" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 28" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 29" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 30" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 31" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 32" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 33" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 34" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 35" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 36" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 37" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 38" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 39" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 40" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 41" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 42" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 43" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 44" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 45" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 46" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 47" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 48" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 49" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 50" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 51" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 52" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 53" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 54" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 55" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 56" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 57" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 58" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 59" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 60" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 61" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 62" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 63" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 64" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 65" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 66" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 67" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 68" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 69" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 70" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 71" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 72" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 73" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 74" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 75" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 76" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 77" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 78" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 79" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 80" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 81" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 82" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 83" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 84" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 85" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 86" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 87" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 88" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 89" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 90" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 91" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 92" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 93" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 94" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 95" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 96" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 97" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 98" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level 99" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A0" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A1" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A2" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A3" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A4" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A5" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A6" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A7" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A8" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level A9" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level B0" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level B1" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    },
    "Level B2" = {
        "req" : "nothing",
        "passwords" : [
            [],
            []
        ],
        "supers" : [
            
        ]
    }
]

def set_all_rules(world: BubbleBobbleWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BubbleBobbleWorld) -> None:
    if world.options.separate_super_bubble_bobble_levels and world.options.lock_super_bubble_bobble_levels:
        unlock_super_bubble_bobble = world.get_entrance("Unlock Super Bubble Bobble")
        world.set_rule(unlock_super_bubble_bobble, lambda state: state.has("Super Bubble Bobble", world.player))

def set_all_location_rules(world: BubbleBobbleWorld) -> None:
    from .locations import levels
    for x in list(levels.keys()):
        
    #########
    #start with if not using separate super levels, then do all the logic under that
    #then else (therefore yes using super levels as separate checks) and do all the logic for that part
    #this is going to be fucking massive

    final_boss = world.get_location("Boss Defeated")
    add_rule(final_boss, lambda state: state.has_all(!!!!!PUT PASSWORDS HERE WITH "or" ENOUGH TO GET THEM ALL TOGETHER))

def set_completion_condition(world: BubbleBobbleWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
