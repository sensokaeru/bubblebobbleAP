from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasAny

from BaseClasses import CollectionState

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
        world.set_rule(world.get_entrance("Unlock Super Bubble Bobble"), Has("Super Bubble Bobble"))

def set_all_location_rules(world: BubbleBobbleWorld) -> None:

    req0 = True_()
    req1 = HasAny("Water Bubbles","Bubble Bounce")
    req2 = Has("Bubble Bounce")
    req3 = HasAny("Lightning Bubbles","Two Player Mode")
    req3b = Has("Lightning Bubbles")
    req4 = HasAny("Water Bubbles","Lightning Bubbles")
    req5 = HasAll("Bubble Bounce","Fire Bubbles")
    req6 = Has("Fire Bubbles")
    req7 = HasAny("Lightning Bubbles","Bubble Bounce")
    req8 = Has("Bubble Bounce") & HasAny("Fire Bubbles","Two Player Mode")
    #req8b = req5
    requirements = [req0, req1, req2, req3, req4, req5, req6, req7, req8, req3b]

    def check_requirement(req):
        setreq = req
        if world.options.lock_two_player_mode and setreq == 3: setreq = 9
        elif if world.options.lock_two_player_mode and setreq == 8: setreq = 5
        return requirements[setreq]

    if not world.options.separate_super_bubble_bobble:
        if not world.options.lock_super_bubble_bobble:
            for level in levels.database:
                passwordreq = False_()
                for password in levels.database.passwords:
                    passwordreq |= HasAll(*password)
                for suppassword in levels.database.supers:
                    passwordreq |= HasAll(*suppassword)
                world.set_rule(world.get_location(level.lev),passwordreq & check_requirement(level.req))
        else:
            for level in levels.database:
                passwordreq = False_()
                suppassreq = False_()
                for password in levels.database.passwords:
                    passwordreq |= HasAll(*password)
                for suppassword in levels.database.supers:
                    suppassreq |= HasAll(*suppassword)
                world.set_rule(world.get_location(level.lev),((suppassreq & Has("Super Bubble Bobble")) | passwordreq) & check_requirement(level.req))
        if world.options.require_best_ending and world.options.lock_two_player_mode: world.set_rule(world.get_location("Boss Defeated"),(CanReachLocation("Level 99") | CanReachLocation("Level B2")) & HasAll("Lightning Bubbles","Drug of Thunder","Two Player Mode"))
        else: world.set_rule(world.get_location("Boss Defeated"),(CanReachLocation("Level 99") | CanReachLocation("Level B2")) & HasAll("Lightning Bubbles","Drug of Thunder"))
    else:
        if not world.options.lock_super_bubble_bobble:
            for level in levels.database:
                passwordreq = False_()
                suppassreq = False_()
                for password in levels.database.passwords:
                    passwordreq |= HasAll(*password)
                for suppassword in levels.database.supers:
                    suppassreq |= HasAll(*suppassword)
                world.set_rule(world.get_location(level.lev),passwordreq & check_requirement(level.req))
                world.set_rule(world.get_location(level.sup),suppassreq & check_requirement(level.req))
        else:
            for level in levels.database:
                passwordreq = False_()
                suppassreq = False_()
                for password in levels.database.passwords:
                    passwordreq |= HasAll(*password)
                for suppassword in levels.database.supers:
                    suppassreq |= HasAll(*suppassword)
                world.set_rule(world.get_location(level.lev),passwordreq & check_requirement(level.req))
                world.set_rule(world.get_location(level.sup),suppassreq & Has("Super Bubble Bobble") & check_requirement(level.req))
        if world.options.require_best_ending and world.options.lock_two_player_mode: world.set_rule(world.get_location("Boss Defeated"),(CanReachLocation("Level 99") | CanReachLocation("Level B2") | CanReachLocation("Super 99") | CanReachLocation("Super B2")) & HasAll("Lightning Bubbles","Drug of Thunder","Two Player Mode"))
        else: world.set_rule(world.get_location("Boss Defeated"),(CanReachLocation("Level 99") | CanReachLocation("Level B2") | CanReachLocation("Super 99") | CanReachLocation("Super B2")) & HasAll("Lightning Bubbles","Drug of Thunder"))
   
def set_completion_condition(world: BubbleBobbleWorld) -> None:

    world.set_completion_rule(Has("Victory"))