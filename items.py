from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from . import levels

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

    def generatestartinglevels():

        first_starting_level = world.random.randrange(len(levels.database))

        while levels.database[first_starting_level].req > 0 or first_starting_level == (len(levels.database) - 1):
            first_starting_level = world.random.randrange(len(levels.database))

        second_starting_level = world.random.randrange(len(levels.database))

        while levels.database[second_starting_level].req > 0 or second_starting_level == first_starting_level or second_starting_level == (len(levels.database) - 1):
            second_starting_level = world.random.randrange(len(levels.database))
        
        third_starting_level = world.random.randrange(len(levels.database))

        while levels.database[third_starting_level].req > 0 or third_starting_level == first_starting_level or third_starting_level == second_starting_level or third_starting_level == (len(levels.database) - 1):
            third_starting_level = world.random.randrange(len(levels.database))

        first_starting_password = levels.database[first_starting_level].passwords[world.random.randrange(len(levels.database[first_starting_level].passwords))]
        second_starting_password = levels.database[second_starting_level].passwords[world.random.randrange(len(levels.database[second_starting_level].passwords))]
        third_starting_password = levels.database[third_starting_level].passwords[world.random.randrange(len(levels.database[third_starting_level].passwords))]

        starting_items = first_starting_password
        for x in second_starting_password:
            if x not in starting_items: starting_items.append(x)

        if len(starting_items) > 10 and not world.options.lock_super_bubble_bobble_levels: return generatestartinglevels()
        elif (len(starting_items) < 11 or len(starting_items) > 13) and world.options.lock_super_bubble_bobble_levels: return generatestartinglevels()
        
        else: return starting_items

    for x in generatestartinglevels():
        itempool.remove(world.create_item(x))
        world.push_precollected(world.create_item(x))

    if world.options.lock_super_bubble_bobble_levels:
        itempool.append(world.create_item("Super Bubble Bobble"))
    if world.options.lock_two_player_mode:
        itempool.append(world.create_item("Two Player Mode"))
    if world.options.increase_starting_lives_count > 0:
        for lives in range(world.options.increase_starting_lives_count):
            itempool.append(world.create_item("Increase Starting Lives"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
