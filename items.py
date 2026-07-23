from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BubbleBobbleWorld

ITEM_NAME_TO_ID = {
    "Timer Trap": 1,
    "Increase Starting Lives": 2,
    "Bubble Bounce": 3,
    "Fire Bubbles": 4,
    "Lightning Bubbles": 5,
    "Water Bubbles": 6,
    "Drug of Thunder": 7,
    "Two Player Mode": 8,
    "Super Bubble Bobble": 9,
    "A - - - -": 10,
    "B - - - -": 11,
    "C - - - -": 12,
    "D - - - -": 13,
    "E - - - -": 14,
    "F - - - -": 15,
    "G - - - -": 16,
    "H - - - -": 17,
    "I - - - -": 18,
    "J - - - -": 19,
    "- A - - -": 20,
    "- B - - -": 21,
    "- C - - -": 22,
    "- D - - -": 23,
    "- E - - -": 24,
    "- F - - -": 25,
    "- G - - -": 26,
    "- H - - -": 27,
    "- I - - -": 28,
    "- J - - -": 29,
    "- - A - -": 30,
    "- - B - -": 31,
    "- - C - -": 32,
    "- - D - -": 33,
    "- - E - -": 34,
    "- - F - -": 35,
    "- - G - -": 36,
    "- - H - -": 37,
    "- - I - -": 38,
    "- - J - -": 39,
    "- - - A -": 40,
    "- - - B -": 41,
    "- - - C -": 42,
    "- - - D -": 43,
    "- - - E -": 44,
    "- - - F -": 45,
    "- - - G -": 46,
    "- - - H -": 47,
    "- - - I -": 48,
    "- - - J -": 49,
    "- - - - A": 50,
    "- - - - B": 51,
    "- - - - C": 52,
    "- - - - D": 53,
    "- - - - E": 54,
    "- - - - F": 55,
    "- - - - G": 56,
    "- - - - H": 57,
    "- - - - I": 58,
    "- - - - J": 59,
    "a popped bubble": 60,
    #####consider adding new filler, like fruit for points, consider extra lives also
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Timer Trap": ItemClassification.trap,
    "Increase Starting Lives": ItemClassification.useful,
    "Bubble Bounce": ItemClassification.progression,
    "Fire Bubbles": ItemClassification.progression,
    "Lightning Bubbles": ItemClassification.progression,
    "Water Bubbles": ItemClassification.progression,
    "Drug of Thunder": ItemClassification.progression,
    "Two Player Mode": ItemClassification.progression,
    "Super Bubble Bobble": ItemClassification.progression,
    "A - - - -": ItemClassification.progression,
    "B - - - -": ItemClassification.progression,
    "C - - - -": ItemClassification.progression,
    "D - - - -": ItemClassification.filler,
    "E - - - -": ItemClassification.progression,
    "F - - - -": ItemClassification.progression,
    "G - - - -": ItemClassification.progression,
    "H - - - -": ItemClassification.filler,
    "I - - - -": ItemClassification.progression,
    "J - - - -": ItemClassification.progression,
    "- A - - -": ItemClassification.progression,
    "- B - - -": ItemClassification.progression,
    "- C - - -": ItemClassification.progression,
    "- D - - -": ItemClassification.progression,
    "- E - - -": ItemClassification.progression,
    "- F - - -": ItemClassification.progression,
    "- G - - -": ItemClassification.progression,
    "- H - - -": ItemClassification.progression,
    "- I - - -": ItemClassification.progression,
    "- J - - -": ItemClassification.progression,
    "- - A - -": ItemClassification.progression,
    "- - B - -": ItemClassification.progression,
    "- - C - -": ItemClassification.progression,
    "- - D - -": ItemClassification.progression,
    "- - E - -": ItemClassification.progression,
    "- - F - -": ItemClassification.progression,
    "- - G - -": ItemClassification.progression,
    "- - H - -": ItemClassification.progression,
    "- - I - -": ItemClassification.progression,
    "- - J - -": ItemClassification.progression,
    "- - - A -": ItemClassification.progression,
    "- - - B -": ItemClassification.progression,
    "- - - C -": ItemClassification.progression,
    "- - - D -": ItemClassification.progression,
    "- - - E -": ItemClassification.progression,
    "- - - F -": ItemClassification.progression,
    "- - - G -": ItemClassification.progression,
    "- - - H -": ItemClassification.progression,
    "- - - I -": ItemClassification.progression,
    "- - - J -": ItemClassification.progression,
    "- - - - A": ItemClassification.filler,
    "- - - - B": ItemClassification.progression,
    "- - - - C": ItemClassification.filler,
    "- - - - D": ItemClassification.progression,
    "- - - - E": ItemClassification.filler,
    "- - - - F": ItemClassification.filler,
    "- - - - G": ItemClassification.progression,
    "- - - - H": ItemClassification.filler,
    "- - - - I": ItemClassification.progression,
    "- - - - J": ItemClassification.progression,
    "a popped bubble": ItemClassification.filler,
}

class BubbleBobbleItem(Item):
    game = "Bubble Bobble"

def get_random_filler_item_name(world: BubbleBobbleWorld) -> str:
    if world.random.randint(0,99) < world.options.timer_trap_chance:
        return "Timer Trap"
    else:
        return "a popped bubble"
        
        #when more filler items are added, add something to randomize them

def create_item_with_correct_classification(world: BubbleBobbleWorld, name: str) -> BubbleBobbleItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return BubbleBobbleItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: BubbleBobbleWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Bubble Bounce"),
        world.create_item("Fire Bubbles"),
        world.create_item("Lightning Bubbles"),
        world.create_item("Water Bubbles"),
        world.create_item("Drug of Thunder"),
        world.create_item("A - - - -"),
        world.create_item("B - - - -"),
        world.create_item("C - - - -"),
        world.create_item("D - - - -"),
        world.create_item("E - - - -"),
        world.create_item("F - - - -"),
        world.create_item("G - - - -"),
        world.create_item("H - - - -"),
        world.create_item("I - - - -"),
        world.create_item("J - - - -"),
        world.create_item("- A - - -"),
        world.create_item("- B - - -"),
        world.create_item("- C - - -"),
        world.create_item("- D - - -"),
        world.create_item("- E - - -"),
        world.create_item("- F - - -"),
        world.create_item("- G - - -"),
        world.create_item("- H - - -"),
        world.create_item("- I - - -"),
        world.create_item("- J - - -"),
        world.create_item("- - A - -"),
        world.create_item("- - B - -"),
        world.create_item("- - C - -"),
        world.create_item("- - D - -"),
        world.create_item("- - E - -"),
        world.create_item("- - F - -"),
        world.create_item("- - G - -"),
        world.create_item("- - H - -"),
        world.create_item("- - I - -"),
        world.create_item("- - J - -"),
        world.create_item("- - - A -"),
        world.create_item("- - - B -"),
        world.create_item("- - - C -"),
        world.create_item("- - - D -"),
        world.create_item("- - - E -"),
        world.create_item("- - - F -"),
        world.create_item("- - - G -"),
        world.create_item("- - - H -"),
        world.create_item("- - - I -"),
        world.create_item("- - - J -"),
        world.create_item("- - - - A"),
        world.create_item("- - - - B"),
        world.create_item("- - - - C"),
        world.create_item("- - - - D"),
        world.create_item("- - - - E"),
        world.create_item("- - - - F"),
        world.create_item("- - - - G"),
        world.create_item("- - - - H"),
        world.create_item("- - - - I"),
        world.create_item("- - - - J"),
    ]

    available_starting_passwords = {
        1 : [["B - - - -","- B - - -","- - A - -","- - - A -","- - - - B"],["B - - - -","- B - - -","- - A - -","- - - B -","- - - - I"],["B - - - -","- B - - -","- - A - -","- - - F -","- - - - B"],["B - - - -","- B - - -","- - A - -","- - - I -","- - - - G"],["B - - - -","- B - - -","- - B - -","- - - A -","- - - - B"],["B - - - -","- B - - -","- - B - -","- - - B -","- - - - B"],["B - - - -","- B - - -","- - B - -","- - - B -","- - - - B"],["B - - - -","- B - - -","- - B - -","- - - I -","- - - - B"],["B - - - -","- B - - -","- - D - -","- - - D -","- - - - D"],["B - - - -","- B - - -","- - D - -","- - - H -","- - - - D"],["B - - - -","- B - - -","- - H - -","- - - H -","- - - - D"]],
        16 : [["A - - - -","- A - - -","- - A - -","- - - A -","- - - - B"],["A - - - -","- A - - -","- - A - -","- - - B -","- - - - I"],["A - - - -","- A - - -","- - A - -","- - - F -","- - - - B"],["A - - - -","- A - - -","- - A - -","- - - I -","- - - - G"],["A - - - -","- A - - -","- - H - -","- - - H -","- - - - D"],["A - - - -","- H - - -","- - A - -","- - - A -","- - - - D"],["A - - - -","- H - - -","- - A - -","- - - F -","- - - - D"],["A - - - -","- H - - -","- - F - -","- - - A -","- - - - I"],["A - - - -","- H - - -","- - F - -","- - - B -","- - - - J"],["A - - - -","- H - - -","- - F - -","- - - F -","- - - - I"],["A - - - -","- H - - -","- - F - -","- - - I -","- - - - B"],["A - - - -","- H - - -","- - F - -","- - - I -","- - - - D"],["A - - - -","- H - - -","- - H - -","- - - D -","- - - - I"],["A - - - -","- H - - -","- - H - -","- - - H -","- - - - B"],["B - - - -","- D - - -","- - B - -","- - - A -","- - - - D"],["B - - - -","- D - - -","- - B - -","- - - B -","- - - - D"],["B - - - -","- D - - -","- - B - -","- - - F -","- - - - D"],["B - - - -","- D - - -","- - B - -","- - - I -","- - - - D"],["B - - - -","- D - - -","- - D - -","- - - D -","- - - - B"],["B - - - -","- D - - -","- - D - -","- - - H -","- - - - B"],["B - - - -","- D - - -","- - I - -","- - - A -","- - - - I"],["B - - - -","- D - - -","- - I - -","- - - B -","- - - - I"],["B - - - -","- D - - -","- - I - -","- - - F -","- - - - I"],["B - - - -","- D - - -","- - I - -","- - - I -","- - - - I"]],
        17 : [["A - - - -","- A - - -","- - B - -","- - - A -","- - - - I"],["A - - - -","- A - - -","- - B - -","- - - B -","- - - - I"],["A - - - -","- A - - -","- - B - -","- - - F -","- - - - G"],["A - - - -","- A - - -","- - B - -","- - - I -","- - - - G"],["A - - - -","- H - - -","- - D - -","- - - D -","- - - - I"],["A - - - -","- H - - -","- - D - -","- - - H -","- - - - I"],["A - - - -","- H - - -","- - I - -","- - - A -","- - - - J"],["A - - - -","- H - - -","- - I - -","- - - B -","- - - - J"],["A - - - -","- H - - -","- - I - -","- - - F -","- - - - B"],["A - - - -","- H - - -","- - I - -","- - - F -","- - - - D"],["A - - - -","- H - - -","- - I - -","- - - I -","- - - - B"],["A - - - -","- H - - -","- - I - -","- - - I -","- - - - D"],["B - - - -","- D - - -","- - A - -","- - - A -","- - - - D"],["B - - - -","- D - - -","- - A - -","- - - F -","- - - - D"],["B - - - -","- D - - -","- - F - -","- - - A -","- - - - I"],["B - - - -","- D - - -","- - F - -","- - - B -","- - - - J"],["B - - - -","- D - - -","- - F - -","- - - F -","- - - - I"],["B - - - -","- D - - -","- - F - -","- - - I -","- - - - B"],["B - - - -","- D - - -","- - F - -","- - - I -","- - - - D"],["B - - - -","- D - - -","- - H - -","- - - D -","- - - - I"],["B - - - -","- D - - -","- - H - -","- - - H -","- - - - B"]],
        18 : [["A - - - -","- B - - -","- - B - -","- - - A -","- - - - I"],["A - - - -","- B - - -","- - B - -","- - - B -","- - - - I"],["A - - - -","- B - - -","- - B - -","- - - F -","- - - - G"],["A - - - -","- B - - -","- - B - -","- - - I -","- - - - G"],["A - - - -","- D - - -","- - D - -","- - - D -","- - - - I"],["A - - - -","- D - - -","- - D - -","- - - H -","- - - - I"],["A - - - -","- D - - -","- - I - -","- - - A -","- - - - J"],["A - - - -","- D - - -","- - I - -","- - - B -","- - - - J"],["A - - - -","- D - - -","- - I - -","- - - F -","- - - - B"],["A - - - -","- D - - -","- - I - -","- - - F -","- - - - D"],["A - - - -","- D - - -","- - I - -","- - - I -","- - - - B"],["A - - - -","- D - - -","- - I - -","- - - I -","- - - - D"],["B - - - -","- H - - -","- - A - -","- - - A -","- - - - D"],["B - - - -","- H - - -","- - A - -","- - - F -","- - - - D"],["B - - - -","- H - - -","- - F - -","- - - A -","- - - - I"],["B - - - -","- H - - -","- - F - -","- - - B -","- - - - J"],["B - - - -","- H - - -","- - F - -","- - - F -","- - - - I"],["B - - - -","- H - - -","- - F - -","- - - I -","- - - - B"],["B - - - -","- H - - -","- - F - -","- - - I -","- - - - D"],["B - - - -","- H - - -","- - H - -","- - - D -","- - - - I"],["B - - - -","- H - - -","- - H - -","- - - H -","- - - - B"]],
        19 : [["A - - - -","- B - - -","- - A - -","- - - A -","- - - - I"],["A - - - -","- B - - -","- - A - -","- - - B -","- - - - J"],["A - - - -","- B - - -","- - A - -","- - - F -","- - - - G"],["A - - - -","- B - - -","- - A - -","- - - I -","- - - - J"],["A - - - -","- D - - -","- - F - -","- - - A -","- - - - J"],["A - - - -","- D - - -","- - F - -","- - - B -","- - - - G"],["A - - - -","- D - - -","- - F - -","- - - F -","- - - - B"],["A - - - -","- D - - -","- - F - -","- - - F -","- - - - D"],["A - - - -","- D - - -","- - F - -","- - - I -","- - - - G"],["A - - - -","- D - - -","- - H - -","- - - D -","- - - - J"],["A - - - -","- D - - -","- - H - -","- - - H -","- - - - I"],["B - - - -","- H - - -","- - D - -","- - - D -","- - - - I"],["B - - - -","- H - - -","- - D - -","- - - H -","- - - - I"],["B - - - -","- H - - -","- - I - -","- - - A -","- - - - J"],["B - - - -","- H - - -","- - I - -","- - - B -","- - - - J"],["B - - - -","- H - - -","- - I - -","- - - F -","- - - - B"],["B - - - -","- H - - -","- - I - -","- - - F -","- - - - D"],["B - - - -","- H - - -","- - I - -","- - - I -","- - - - B"],["B - - - -","- H - - -","- - I - -","- - - I -","- - - - D"]],
        52 : [["F - - - -","- A - - -","- - A - -","- - - A -","- - - - J"],["F - - - -","- A - - -","- - A - -","- - - B -","- - - - G"],["F - - - -","- A - - -","- - A - -","- - - F -","- - - - J"],["F - - - -","- A - - -","- - F - -","- - - B -","- - - - B"],["F - - - -","- A - - -","- - F - -","- - - B -","- - - - D"],["F - - - -","- H - - -","- - C - -","- - - G -","- - - - G"],["F - - - -","- H - - -","- - F - -","- - - A -","- - - - G"],["F - - - -","- H - - -","- - F - -","- - - F -","- - - - G"],["F - - - -","- H - - -","- - F - -","- - - I -","- - - - J"],["F - - - -","- H - - -","- - H - -","- - - D -","- - - - G"],["F - - - -","- H - - -","- - H - -","- - - H -","- - - - J"],["I - - - -","- D - - -","- - D - -","- - - D -","- - - - J"],["I - - - -","- D - - -","- - D - -","- - - H -","- - - - J"],["I - - - -","- D - - -","- - I - -","- - - A -","- - - - G"],["I - - - -","- D - - -","- - I - -","- - - B -","- - - - G"],["I - - - -","- D - - -","- - I - -","- - - F -","- - - - G"],["I - - - -","- D - - -","- - I - -","- - - I -","- - - - G"]],
        53 : [["F - - - -","- A - - -","- - B - -","- - - A -","- - - - G"],["F - - - -","- A - - -","- - B - -","- - - B -","- - - - G"],["F - - - -","- A - - -","- - B - -","- - - H -","- - - - G"],["F - - - -","- A - - -","- - I - -","- - - A -","- - - - B"],["F - - - -","- A - - -","- - I - -","- - - A -","- - - - D"],["F - - - -","- A - - -","- - I - -","- - - B -","- - - - B"],["F - - - -","- A - - -","- - I - -","- - - B -","- - - - D"],["F - - - -","- H - - -","- - D - -","- - - D -","- - - - G"],["F - - - -","- H - - -","- - D - -","- - - H -","- - - - G"],["F - - - -","- H - - -","- - I - -","- - - F -","- - - - J"],["F - - - -","- H - - -","- - I - -","- - - I -","- - - - J"],["F - - - -","- H - - -","- - J - -","- - - E -","- - - - G"],["F - - - -","- H - - -","- - J - -","- - - G -","- - - - G"],["I - - - -","- D - - -","- - C - -","- - - G -","- - - - G"],["I - - - -","- D - - -","- - F - -","- - - A -","- - - - G"],["I - - - -","- D - - -","- - F - -","- - - F -","- - - - G"],["I - - - -","- D - - -","- - F - -","- - - I -","- - - - J"],["I - - - -","- D - - -","- - H - -","- - - D -","- - - - G"],["I - - - -","- D - - -","- - H - -","- - - H -","- - - - J"]],
        55 : [["F - - - -","- B - - -","- - A - -","- - - A -","- - - - G"],["F - - - -","- B - - -","- - A - -","- - - B -","- - - - D"],["F - - - -","- B - - -","- - A - -","- - - I -","- - - - D"],["F - - - -","- B - - -","- - F - -","- - - A -","- - - - B"],["F - - - -","- B - - -","- - F - -","- - - A -","- - - - D"],["F - - - -","- B - - -","- - F - -","- - - B -","- - - - I"],["F - - - -","- B - - -","- - F - -","- - - I -","- - - - I"],["F - - - -","- B - - -","- - H - -","- - - D -","- - - - B"],["F - - - -","- D - - -","- - C - -","- - - E -","- - - - G"],["F - - - -","- D - - -","- - C - -","- - - G -","- - - - J"],["F - - - -","- D - - -","- - C - -","- - - J -","- - - - J"],["F - - - -","- D - - -","- - F - -","- - - F -","- - - - J"],["F - - - -","- D - - -","- - H - -","- - - H -","- - - - G"],["I - - - -","- H - - -","- - D - -","- - - D -","- - - - G"],["I - - - -","- H - - -","- - D - -","- - - H -","- - - - G"],["I - - - -","- H - - -","- - I - -","- - - F -","- - - - J"],["I - - - -","- H - - -","- - I - -","- - - I -","- - - - J"],["I - - - -","- H - - -","- - J - -","- - - E -","- - - - G"],["I - - - -","- H - - -","- - J - -","- - - G -","- - - - G"]]
    }

    available_starting_levels = list(available_starting_passwords.keys())
    starting_level = available_starting_levels[world.random.randrange(len(available_starting_levels))]
    possible_passwords = available_starting_passwords[starting_level]
    starting_password = possible_passwords[world.random.randrange(len(possible_passwords))]

    for x in starting_password:
        itempool.remove(world.create_item(x))
        world.push_precollected(x)

    if world.options.lock_super_bubble_bobble_levels:
        itempool.add(world.create_item("Super Bubble Bobble"))
    if world.options.lock_two_player_mode:
        itempool.add(world.create_item("Two Player Mode"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
