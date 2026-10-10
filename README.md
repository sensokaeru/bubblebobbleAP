# Bubble Bobble for Archipelago

## Required software

- BizHawk: [BizHawk Releases from TASVideos](https://tasvideos.org/BizHawk/ReleaseHistory)
  - This has only been tested in version 2.9.1.  I do not know if other versions will work.
  - Detailed installation instructions for BizHawk can be found at the above link.
  - Windows users must run the prereq installer first, which can also be found at the above link.
- The built-in Archipelago BizHawk client, which can be installed [here](https://github.com/ArchipelagoMW/Archipelago/releases)
- An NES Bubble Bobble (US) ROM file

## How is progression locked in Bubble Bobble?

- This Bubble Bobble apworld prevents you from playing a level if you don't have the letters to enter a password that goes to that level.
- You'll start with enough letters to enter at least 2 levels.
- You send a check whenever you beat a level.
- Some levels require unlocking Bubble Bounce or the elemental (fire, water, lightning) bubbles in order to complete them.  Items locking those abilities are shuffled into the item pool.
- If Super Bubble Bobble levels or Two Player Mode are locked, those levels will also require items that are shuffled into the item pool to unlock them.
- If Two Player Mode is locked, a few levels can potentially logically require Two Player Mode to complete them.
- Find the Drug of Thunder, Lightning Bubbles, and the letters for a password to get to either Level 99 or Level B2 in order to move on to the boss fight and complete the game.

## Known issues

- Bubble Bounce is locked until you find the item to unlock it, but even when it is locked, you can still bounce if you press the jump button with good timing.  You won't bounce if you're holding down the jump button to do so.  I have no idea what is causing this issue.
- In the previous version, there was a bug that would force a game over even when loading a level, even though you should be able to access it.  Code was modified to fix this, but it has not been thoroughly tested yet.
- Death Links send, but receiving them was not working in the previous version.  I've applied a fix, but not yet tested it.

## Notes about the password locking system

- The vanilla game gives you exactly one password per level, but in actuality, every level has several passwords that work.  Every password that works in the AP will also work in the vanilla game.
- By default, a Super Bubble Bobble level is the same check as a regular level.  Super Bubble Bobble levels can be made into separate checks by enabling the Separate Super Bubble Bobble option in the yaml.
- Use the /find_level command in the client to find a valid password that you can currently use.
- If you enter a level and immediately game over, that means you don't have a password you can use for that level right now.
- It is ***highly*** recommended that you use this in conjunction with Universal Tracker to know what levels you should be able to go to.  In fact, this might be relatively unplayable without it.

## Special thanks

- Thanks to Ehseezed and Rawsome for helping me get the original manual Bubble Bobble apworld working, which inspired this project.
- Biggest thanks ever to HappyHappyism for babying me through the very little NES ASM that I needed to understand to piece together part of this and for all his help with the Python code, too.
- To NewSoupVi for the very educational comments in the APQuest code.
- Also thanks to Thedragon005 for explaining how Github works, contributing code, and pointing out obvious things that I simply did not manage to figure out on my own.
- And thanks to the unbelievably patient denizens of #ap-world-dev for tolerating the extreme depths of my ignorance.
