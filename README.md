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
- Some levels require unlocking Bubble Bounce or the elemental (fire, water, lightning) bubbles in order to complete them.
- If Super Bubble Bobble levels are locked, those levels will also require a Super Bubble Bobble item.
- Find the Drug of Thunder and a password to go to either Level 99 or Level B2 in order to move on to the boss fight and complete the game.

## Known issues

- Skill locks (Bubble Bounce, the elemental bubbles, and the Drug of Thunder) are currently on the honor system.  The logic is written for generation's sake, but the client interaction that actually locks those things down is not written yet.
- Occasionally, a check just does not send.  Try beat the level a few more times to send the check if this happens.
- Separating and locking Super levels are untested.
- There was a bug with modifying starting levels that made enemies act really weird.  I've applied a fix, but this is not yet tested.

## Notes about the password locking system

- The vanilla game gives you exactly one password per level, but in actuality, every level has several passwords that work.  Every password that works in the AP will also work in the vanilla game.
- If you enter a level and immediately game over, that means you don't have a password you can use for that level right now.

## Special thanks

- Thanks to Ehseezed and Rawsome for helping me get the original manual Bubble Bobble apworld working, which inspired this project.
- Big thanks to HappyHappyism for babying me through the very little NES ASM that I needed to understand to piece together part of this.
- And thanks to the unbelievably patient denizens of #ap-world-dev for tolerating the extreme depths of my ignorance.
