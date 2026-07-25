from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from . import levels
#call levels data as levels.database

if TYPE_CHECKING:
    from .world import BubbleBobbleWorld

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
