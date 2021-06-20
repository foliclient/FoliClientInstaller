#!/usr/bin/env python3

# Foli Client Installer v1.2.1 for Minecraft 1.16.5
# Script by ablazingeboy#7375
# Other credits in README.md

# Imports
import sys
import os
import shutil
import argparse
import urllib.request
import zipfile

# Argparse magic
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Specify a specific directory to install to. If this argument isn't used, the installer will prompt you for the destination directory.")
parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Adds extra logs")
graphicsmods = parser.add_mutually_exclusive_group()
graphicsmods.add_argument("--optifine", action="store_true", default=False, help="Adds Optifine in place of Sodium, and removes conflicting/redundant mods. Optifine is not recommended, as due to modifications in this pack Sodium performs significantly faster, however it does have shader support.")
graphicsmods.add_argument("--sodium", action="store_true", default=False, help="Bypasses the prompt asking whether to use Optifine or Sodium, and adds Sodium.")
extrasargs = parser.add_mutually_exclusive_group()
extrasargs.add_argument("--extras", action="store_true", default=False, help="Downloads and installs the foli-extras package. Requires an internet connection.")
extrasargs.add_argument("--noextras", action="store_true", default=False, help="Bypasses the prompt asking whether to install foli-extras, and does not install foli-extras.")
parser.add_argument("--astral", help=argparse.SUPPRESS, action="store_true", default=False)
args = parser.parse_args()

# Set variables based on args
use_optifine = args.optifine
install_extras = args.extras

# Helper Methods
def get_full_path(relpath):
    # Takes a relative path and converts it to an absolute path, and validates said path
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller onefile compatibility
        os.chdir(sys._MEIPASS)
        fullpath = os.path.join(sys._MEIPASS, relpath)
    else:
        fullpath = os.path.abspath(os.path.join(os.path.dirname(__file__), relpath))

    if not os.path.isdir(fullpath):
        print(f'[ERROR]\t{fullpath} is missing. Please re-download the package or make sure the resources folder is in the same folder as this program and has not been altered.')
        print('\n[INPUT]\tPress any key to exit...')
        input()
        sys.exit()
    else:
        print(f'[LOG]\tValidated {relpath}')
        return fullpath

def copydir(sourcedir, destdir):
    # Walks the given folder and copies all files and subdirectories to the destination
    for subdir, dirs, files in os.walk(sourcedir):
        for filename in files:
            filepath = subdir + os.sep + filename
            destination = subdir.replace(sourcedir, '')
            os.makedirs(destdir + destination, exist_ok=True)
            fulldestpath = destpath + destination + os.sep + filename
            shutil.copyfile(filepath, fulldestpath)
            if(args.verbose):
                print(f'[LOG]\tCopied {destination + os.sep + filename} to {fulldestpath}')

def pull_zip(label, url, destdir):
    if args.verbose:
        print(f'\n[LOG]\tDownloading {label} from {url}...')
    else:
        print(f'\n[LOG]\tDownloading {label}...')
    zip_path, _ = urllib.request.urlretrieve(url)
    if args.verbose:
        print(f'[LOG]\tExtracting {label} to {destdir}...')
    else:
        print(f'[LOG]\tExtracting {label}...')
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(destdir)

# ASCII Title
print('\n\'||\'\'\'\'|        \'||`      .|\'\'\'\', \'||`                        ||    \n ||  .           ||   \'\'  ||       ||   \'\'                    ||    \n ||\'\'|   .|\'\'|,  ||   ||  ||       ||   ||  .|\'\'|, `||\'\'|,  \'\'||\'\'  \n ||      ||  ||  ||   ||  ||       ||   ||  ||..||  ||  ||    ||    \n.||.     `|..|\' .||. .||. `|....\' .||. .||. `|...  .||  ||.   `|..\' \n')
# Remember to change version flag and mc version when updating!
print('Installing Foli Client v1.2.1 for Minecraft 1.16.5')
print('Installer made with <3 by ablazingeboy#7375')
print('Learn more or submit any issues at https://github.com/ablazingeboy/FoliClientInstaller\n')
print('While unlikely, this program has the chance of screwing up your system if used incorrectly.\nI AM NOT RESPONSIBLE FOR ANY DATA LOSS INCURRED BY USING THIS SCRIPT.\nFor best results, use this on a fresh minecraft profile, and Fabric MUST be installed.\n')

# Sets or asks for what path to install to
destPath = ''
if args.directory:
    destpath = args.directory
else:
    print('[INPUT]\tPlease type in the full filepath of your .minecraft folder:')
    destpath = input()

# Validates that the installation path is valid
isdir = os.path.isdir(destpath)
if not isdir:
    print(f'[ERROR]\tUh oh, \"{destpath}\" is not a folder on your computer! Please check for any typos!')
    print('\n[INPUT]\tPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\t' + destpath + ' is a valid directory')

    # Prompts user to confirm install directory
    confirmedDir = False
    while confirmedDir == False:
        print(f'\n[INPUT]\tAre you sure you want to install to \"{destpath}\"? (Y\\N)')
        choice = input().lower()
        if choice == 'y':
            confirmedDir = True
        elif choice == 'n':
            print('\n[INPUT]\tPress any key to exit...')
            input()
            sys.exit()
        else:
            print('[ERROR]\tNot a valid choice, please try again!')

# Asks the user if they want to use Optifine
if (not args.optifine and not args.sodium):
    loop_prompt=True
    while(loop_prompt):
        print(f'\n[INPUT]\tYou can choose to use Optifine in place of Sodium on Foli Client. Sodium is generally recommended for most users, as the performance even on old hardware far outclasses Optifine, thanks to mods included in Foli Client. However, Optifine has shader support, so if you want to use those, choose Optifine.\nDo you want to use Optifine? (Y/N)')
        choice = input().lower()
        if choice == 'y':
            use_optifine = True
            loop_prompt = False
        elif choice == 'n':
            use_optifine = False
            loop_prompt = False
        else:
            print(f'\n[ERROR]\t{choice} is not a valid selection.')

# Asks the user if they want to download foli-extras
if(not args.extras and not args.noextras):
    loop_prompt=True
    while(loop_prompt):
        print(f'\n[INPUT]\tWould you like to download foli-extras? foli-extras is a collection of extra resourcepacks and other assets. For a full list of what is included, refer to the README. Downloading foli-extras requires an internet connection.\nDo you want to download foli-extras? (Y/N)')
        choice = input().lower()
        if choice == 'y':
            install_extras = True
            loop_prompt = False
        elif choice == 'n':
            install_extras = False
            loop_prompt = False
        else:
            print(f'\n[ERROR]\t{choice} is not a valid selection.')

# Validates and copies files
commonpath = get_full_path(os.path.join('resources', 'common'))
copydir(commonpath, destpath)
if(use_optifine):
    optifinepath = get_full_path(os.path.join('resources', 'optifine'))
    copydir(optifinepath, destpath)
else:
    sodiumpath = get_full_path(os.path.join('resources', 'sodium'))
    copydir(sodiumpath, destpath)

if(install_extras):
    pull_zip('foli-extras', "https://github.com/foliclient/foli-extras/archive/refs/heads/main.zip", destpath)
    extraspath = os.path.join(destpath, 'foli-extras-main')
    copydir(extraspath, destpath)
    print(f'\n[LOG]\tDeleting temp download folder')
    shutil.rmtree(extraspath)

if args.astral:
    print('\n[MESSAGE]\tWAKE THE FUCK UP ASTRAL WE\'RE GOING TO THE FUCKING STARS WOOOOOOOOOOOOOOOO')
    os.rename(destpath + os.sep + 'config' + os.sep + 'bg.jpg', destpath + os.sep + 'config' + os.sep + 'bgoriginal.jpg')
    os.rename(destpath + os.sep + 'config' + os.sep + 'astral.jpg', destpath + os.sep + 'config' + os.sep + 'bg.jpg')

# Success Message
print('\n[LOG]\tAll files have been copied over, and Foli Client should now be installed. Remember to turn on the resourcepack!')
print('\n[INPUT]\tPress any key to exit...')
input()
sys.exit()
