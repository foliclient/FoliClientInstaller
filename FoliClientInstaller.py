# Foli Client Installer v1.0.1 for Minecraft 1.16.4/5
# Script by ablazingeboy#7375
# Other credits in README.md

# Imports
import sys
import os
from os import path
import shutil

# ASCII Title
print('\n\'||\'\'\'\'|        \'||`      .|\'\'\'\', \'||`                        ||    \n ||  .           ||   \'\'  ||       ||   \'\'                    ||    \n ||\'\'|   .|\'\'|,  ||   ||  ||       ||   ||  .|\'\'|, `||\'\'|,  \'\'||\'\'  \n ||      ||  ||  ||   ||  ||       ||   ||  ||..||  ||  ||    ||    \n.||.     `|..|\' .||. .||. `|....\' .||. .||. `|...  .||  ||.   `|..\' \n')
# Remember to change version flag and mc version when updating!
print('Installing Foli Client v1.0.1 for Minecraft 1.16.4/5')
print('Installer made with <3 by ablazingeboy#7375')
print('Learn more or submit any issues at https://github.com/ablazingeboy/FoliClientInstaller\n')
print('While unlikely, this program has the chance of screwing up your system if used incorrectly.\nI AM NOT RESPONSIBLE FOR ANY DATA LOSS INCURRED BY USING THIS SCRIPT.\nFor best results, use this on a fresh minecraft profile, and Fabric MUST be installed.\n')

# Sets or asks for what path to install to
destPath = ''
if len(sys.argv) == 2:
    destpath = sys.argv[1]
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

# Makes sure the resources folder exists
sourcepath = path.abspath(path.join(path.dirname(__file__), 'resources'))
if not os.path.isdir(sourcepath):
    print('[ERROR]\tCan\'t find the resources folder. Please re-download the package or make sure the resources folder is in the same folder as this program')
    print('\n[INPUT]\tPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\tValidated resource directory')

# Walks the resource directory and copies files
print('\n')
for subdir, dirs, files in os.walk(sourcepath):
    for filename in files:
        filepath = subdir + os.sep + filename
        destination = subdir.replace(sourcepath, '')
        os.makedirs(destpath + destination, exist_ok=True)
        fulldestpath = destpath + destination + os.sep + filename
        shutil.copyfile(filepath, fulldestpath)
        print(f'[LOG]\tCopied {destination} to {fulldestpath}')

# Success Message
print('\n[LOG]\tAll files have been copied over, and Foli Client should now be installed. Remember to turn on the resourcepack!')
print('\n[INPUT]\tPress any key to exit...')
input()
sys.exit()