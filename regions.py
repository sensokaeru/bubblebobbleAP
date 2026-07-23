from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BubbleBobbleWorld

def create_and_connect_regions(world: BubbleBobbleWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BubbleBobbleWorld) -> None:
    bubblebobble = Region("Bubble Bobble", world.player, world.multiworld)

    regions = [bubblebobble]

    if world.options.separate_super_bubble_bobble_levels:
        superbubblebobble = Region("Super Bubble Bobble", world.player, world.multiworld)
        regions.append(superbubblebobble)

    world.multiworld.regions += regions

def connect_regions(world: BubbleBobbleWorld) -> None:
    bubblebobble = world.get_region("Bubble Bobble")

    if world.options.separate_super_bubble_bobble_levels:
        superbubblebobble = world.get_region("Super Bubble Bobble")
        bubblebobble.connect(superbubblebobble, "Unlock Super Bubble Bobble")
        