![](https://github.com/foliclient/FoliClientInstaller/raw/1.16.x/resources/common/config/foliclientlogobg.png)

![](https://img.shields.io/github/downloads/foliclient/FoliClientInstaller/total?style=for-the-badge)

For more information about Foli Client, please visit the [website](https://foliclient.astral.vip).

## What is Foli Client?

Foli Client is a customized, preconfigured modpack intended to provide players with useful tools for technical Minecraft. In addition, mods are configured by default to be legal on the TeenagersGaming Minecraft Server. Here is an explanation of some of the various mods included:

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
