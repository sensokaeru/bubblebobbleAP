from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink

class SuperLevels(Toggle):
    """
    By default, beating a Super Bubble Bobble level gives you the same check as if you had beaten a normal Bubble Bobble level.
    Turn this on to set the Super Bubble Bobble levels as separate checks instead, doubling the available checks in the game.
    """

    display_name = "Separate Super Bubble Bobble levels"

class LockSupers(Toggle):
    """
    Turn this on to require a Super Bubble Bobble item to unlock Super Bubble Bobble levels.
    Enabling this causes you to start with additional starting levels due to restricting the logic too much.
    """

    display_name = "Lock Super Bubble Bobble levels"

class LockTwoPlayer(Toggle):
    """
    Turn this on to require a Two Player Mode item to unlock Two Player Mode.
    WARNING!!! This CAN be logically required for some levels.
    """

    display_name = "Lock Two Player Mode"

class EndingReq(Toggle):
    """
    Turn this on to require the best ending rather than any ending.
    WARNING!!!  This REQUIRES beating the game in two player mode.
    """

    display_name = "Require Best Ending"

class IncreaseLivesWeight(Range):
    """
    Weighted chance that a filler item is replaced with an Increase Starting Lives item.
    The starting lives is set to 3 by default.
    Each Increase Starting Lives item increases the starting lives by 1.
    Note: Lives over 10 cause a minor graphical bug that does not seem to affect gameplay.
    """

    display_name = "Increase Starting Lives Weight"
    range_start = 0
    range_end = 100
    default = 5

class TimerTrapWeight(Range):
    """
    Weighted chance that a filler item is replaced with a Timer Trap.
    """

    display_name = "Timer Trap Weight"
    range_start = 0
    range_end = 100
    default = 20

class FillerWeight(Range):
    """
    Weighted chance that a filler item will be a popped bubble, which does nothing.
    Note: If the combined value of the three weighted options is 0, every filler item will become a popped bubble.
    """

    display_name = "Filler Weight"
    range_start = 0
    range_end = 100
    default = 40

class DeathLinkTrigger(Toggle):
    """
    Determines what triggers a death link.  Turn this ON to trigger a death link every time you lose a life.
    Turn this OFF to trigger a death link only on game over.
    This is ignored if Death Link is off.
    """
    display_name = "Death Link Every Death"

class DeathLinkResult(Toggle):
    """
    Determines the result of a death link.  Turn this ON to game over every time a death link is received.
    Turn this OFF to only lose one life every time a death link is received.
    This is ignored if Death Link is off.
    """
    display_name = "Death Link Causes Game Over"


@dataclass
class BubbleBobbleOptions(PerGameCommonOptions):
    separate_super_bubble_bobble_levels: SuperLevels
    lock_super_bubble_bobble_levels: LockSupers
    lock_two_player_mode: LockTwoPlayer
    require_best_ending: EndingReq
    increase_starting_lives_weight: IncreaseLivesWeight
    timer_trap_weight: TimerTrapWeight
    filler_weight: FillerWeight
    deathlink: DeathLink
    deathlinktrigger: DeathLinkTrigger
    deathlinkresult: DeathLinkResult

option_groups = [
    OptionGroup(
        "Progression Options",
        [SuperLevels, LockSupers, LockTwoPlayer, EndingReq],
    ),
    OptionGroup(
        "Filler Options",
        [IncreaseLivesWeight, TimerTrapWeight, FillerWeight]
    ),
    OptionGroup(
        "Death Link Options",
        [DeathLink, DeathLinkTrigger, DeathLinkResult]
    )
]

option_presets = {
    "easiest": {
        "separate_super_bubble_bobble_levels": False,
        "lock_super_bubble_bobble_levels": False,
        "lock_two_player_mode": False,
        "require_best_ending": False,
        "increase_starting_lives_weight": 20,
        "timer_trap_weight": 0,
        "filler_weight": 30,
        "deathlink": False,
        "deathlinktrigger": False,
        "deathlinkresult": False,
    },
    "hardest": {
        "separate_super_bubble_bobble_levels": True,
        "lock_super_bubble_bobble_levels": True,
        "lock_two_player_mode": True,
        "require_best_ending": True,
        "increase_starting_lives_weight": 0,
        "timer_trap_weight": 100,
        "filler_weight": 0,
        "deathlink": True,
        "deathlinktrigger": True,
        "deathlinkresult": True,
    },
    "balanced co-op": {
        "separate_super_bubble_bobble_levels": False,
        "lock_super_bubble_bobble_levels": False,
        "lock_two_player_mode": False,
        "require_best_ending": True,
        "increase_starting_lives_weight": 7,
        "timer_trap_weight": 20,
        "filler_weight": 30,
        "deathlink": True,
        "deathlinktrigger": False,
        "deathlinkresult": False,
    },
}