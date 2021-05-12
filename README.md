![](https://raw.githubusercontent.com/ablazingeboy/FoliClientInstaller/main/resources/config/foliclientlogobg.png?token=AS4NPFVUY4OGEDUZH4RM273ANR72C)

![](https://img.shields.io/github/downloads/ablazingeboy/FoliClientInstaller/total?style=for-the-badge)

This is the installer for the Foli Client modpack.

## What is Foli Client?

Foli Client is a customized, preconfigured modpack intended to provide a player with useful tools for technical Minecraft. In addition, mods are configured by default to be legal on the TeenagersGaming Minecraft Server. Here is an explanation of some of the various mods included:

| Mod                                   | What it does                                                 |
| ------------------------------------- | ------------------------------------------------------------ |
| InventoryHUD+                         | Displays your inventory, armor status, and potion effects in HUDs |
| VoxelMap                              | Gives you a minimap and a worldmap that updates as you explore.\*\*\* (Note: the hotkey to open the world map has been changed from `m` to `` ` ``) |
| MiniHUD                               | Displays FPS, Ping, Memory Usage, and more in a highly configurable HUD |
| Also MiniHUD                  | Displays the full contents of a shulker box when you hold `shift` and hover over it in your inventory |
| Also MiniHUD                         | Shows the light level of the blocks around you. Toggled using `f7`. |
| Litematica                            | Allows you to make schematics of builds, and display them as an overlay in game to help recreate a build. Note that the execution hotkey is set to `f6`|
| ReplayMod                             | Allows you to record gameplay, and view it as if in spectator mode later.\*\* |
| DynamicFPS, Sodium/Optifine\*\*\*\*, Lithium\*\*\*\*, Phosphor | Increase Minecraft performance significantly                 |
| Ok Zoomer/Optifine\*\*\*\* | Allows you to zoom, activated by holding `C` |
| MyBrightness | FullBright, turn it on using `5` on the numpad (You can remap this in the ingame hotkey settings) |

## Installation Instructions

Terrible video tutorial: https://youtu.be/bCiTwZmqE7A
(Note that the tutorial shows downloading the 'source code' folder, but as of Foli Client Installer 1.1.0, the exe is released as a standalone file on the Releases page)

1. Create a **fresh** profile/instance of Minecraft. If using the default launcher, it is recommended to create a different installation directory for the profile you will be using for Foli Client. **I strongly suggest using MultiMC**, as it makes it easy to manage multiple Minecraft profiles, and allows you to install Fabric with one click.
2. Install [Fabric](https://fabricmc.net/). **Do not install Fabric API**, as the appropriate version is included in the modpack.
3. Download the latest release from the [Releases](https://github.com/ablazingeboy/FoliClientInstaller/releases) page. If on Windows, download the .exe file. If on MacOS or Linux, download the 'source code' zip and unzip it. Do not move any of the files from the folder where they were unzipped.
4. Run the installer for your OS (`FoliClientInstaller.exe` for Windows, and `FoliClientInstaller.py`\* for other platforms). When prompted, paste in the **full filepath** of your Minecraft install directory (e.g. `C:\Users\ABlazingEBoy\Documents\MinecraftDirectory` on Windows or  `/Users/ABlazingEBoy/Documents/MinecraftDirectory` on Mac)
5. After you start up Foli Client, **make sure to apply the two included resource packs. Foli Client Specific Textures should always be on top of your resourcepack list for the client to look correct**
6. Enjoy Foli Client! 

## Notes

- \*The Python script is written for Python 3.9, and *should* work on any OS, though it has only been tested on Windows and MacOS.
- \*If clicking the script brings up an error, try running it by opening a termnal in the folder and running `python3 FoliClientInstaller.py`
- If you don't want to run the installer, you can also just manually copy all of the folders in the `resources` folder in the zip to your Minecraft install directory
- \*\*ReplayMod is included, but autorecording is disabled by default. If you're using it on TG, remember not to abuse it to see where you shouldn't, or gain any unfair advantage.
- \*\*ReplayMod depends on FFmpeg to function correctly. The FFmpeg executable has been included, meaning Windows users don't need to do anything, however, if you're on a Mac or Linux machine you will need to install FFmpeg manually. For more info go to [Replaymod's website](https://www.replaymod.com/).
- \*\*\*Voxelmap's Menu key has been remapped from `m` to `` ` `` (the one above `Tab` on English keyboards), and Cave Mode and Radar have been disabled.
- \*\*\*\*If the installer is run with the `--optifine` argument, or you choose it during the install process, Sodium, Lithium, and Ok Zoomer will be replaced with Optifine and Optifabric.
- To activate the Light Overlay, press `f7`
- The installer has CLI arguments if you want to use those rather than manually entering values during the install process. To see the available arguments, run `FoliClientInstaller.exe -h` or `FoliClientInstaller.py -h`.
- If you have any issues with the installer, submit a GitHub issue or message me on Discord at ablazingeboy#7375

## Credits

Thanks to AydenSWG for making custom textures for the included resource pack.

Thanks to WinterStars, exgodstatus, and TheDoctor7562 for giving me insight on their mod configs, and providing suggestions for configuring mods.

## Mods Used

- [Fabric API](https://www.curseforge.com/minecraft/mc-mods/fabric-api)
- [Custom Window Title](https://www.curseforge.com/minecraft/mc-mods/custom-window-title)
- [Voxelmap](https://www.curseforge.com/minecraft/mc-mods/voxelmap)
- [Sodium](https://www.curseforge.com/minecraft/mc-mods/sodium)
- [Lithium](https://www.curseforge.com/minecraft/mc-mods/lithium)
- [Phosphor](https://www.curseforge.com/minecraft/mc-mods/phosphor)
- [FancyMenu](https://www.curseforge.com/minecraft/mc-mods/fancymenu-fabric)
- [Dynamic FPS](https://www.curseforge.com/minecraft/mc-mods/dynamic-fps)
- [Inventory HUD+](https://www.curseforge.com/minecraft/mc-mods/inventory-hud-forge)
- [MiniHUD](https://www.curseforge.com/minecraft/mc-mods/minihud)
- [Litematica](https://www.curseforge.com/minecraft/mc-mods/litematica)
- [CraftPresence](https://www.curseforge.com/minecraft/mc-mods/craftpresence)
- [ReplayMod](https://www.replaymod.com/)
- [FFmpeg](https://ffmpeg.org/)
- [MyBrightness](https://www.curseforge.com/minecraft/mc-mods/mybrightness)
- [Ok Zoomer](https://www.curseforge.com/minecraft/mc-mods/ok-zoomer)
- [Optifine](https://www.optifine.net/home)
- [Optifabric](https://www.curseforge.com/minecraft/mc-mods/optifabric)

## Resource Packs Used

- Most tweaks from [VanillaTweaks for 1.16](https://vanillatweaks.net/)
- Wither and Wither Skeleton texture from [TG Resource Pack](https://drive.google.com/file/d/17eHH_U8ujffCjJJlVBGVNYmlaor1u1dz/view?usp=sharing)
- Custom textures by AydenSWG

## Build

If for some ungodly reason you want to build the exe from source, install PyInstaller from pip, navigate to the cloned repo, then run `pyinstaller --onefile --icon=Icon32.ico --distpath=. --add-data "resources;resources" FoliClientInstaller.py`.
