#!/usr/bin/env python3

# Imports
import sys
import os
import shutil
import argparse
import PySimpleGUI as sg

# Variables
version = '2.1.0'
mcversion = '1.17.1'
sg.theme('DarkBrown1')

# Argparse magic
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Specify a specific directory to install to. If this argument isn't used, the installer will prompt you for the destination directory.")
graphicsmods = parser.add_mutually_exclusive_group()
graphicsmods.add_argument("--optifine", action="store_true", default=False, help="Bypasses the prompt asking which graphics mod to use, and adds OptiFine. (Not recommended for most users)")
graphicsmods.add_argument("--sodium", action="store_true", default=False, help="Bypasses the prompt asking which graphics mod to use, and adds Sodium with Sodium Extra. (Recommended for most users)")
graphicsmods.add_argument("--iris", action="store_true", default=False, help="Bypasses the prompt asking which graphics mod to use, and adds Sodium with Iris. (Recommended for users who want shaders)")
parser.add_argument("--astral", help=argparse.SUPPRESS, action="store_true", default=False)
args = parser.parse_args()

# Set variables based on args
use_optifine = args.optifine
use_iris = args.iris

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
        error_popup(f'{fullpath} is missing. Please re-download the package or make sure the resources folder is in the same folder as this program and has not been altered.')
    else:
        message_log(f'Validated {relpath}')
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
            file_log(f'Copied {destination + os.sep + filename} to {fulldestpath}')

def error_popup(error):
    error_log(error)
    sg.Window('Error!', [[sg.T(error)], [sg.Exit()]], disable_close=True).read(close=True)
    sys.exit()

def exit_popup():
    sg.Window('Installer Exited', [[sg.T('The installer has been exited and no changes have been made.')], [sg.Exit()]], disable_close=True).read(close=True)
    sys.exit()

def message_log(message):
    print(f'[LOG]\t{message}')

def error_log(error):
    print(f'[ERROR]\t{error}')

def file_log(text):
    print(f'[FILE_WRITE]\t{text}')

def custom_log(type, message):
    print(f'[{type}]\t{message}')

# Sets or asks for what path to install to
if args.directory:
    destpath = args.directory
else:
    event, values = sg.Window(f'Foli Client Installer v{version}', [[sg.T(f'Welcome to the Foli Client Installer for Minecraft {mcversion}!\nPlease read the instructions on the website before installing!')],
                                                                    [sg.T('While unlikely, this program has the chance of screwing up your system if used incorrectly.\nI AM NOT RESPONSIBLE FOR ANY DATA LOSS INCURRED BY USING THIS SCRIPT.\nFor best results, use this on a fresh minecraft profile, and Fabric MUST be installed.')],
                                                                    [sg.T('Installer made with <3 by ablazingeboy#7375\nWebsite: https://foliclient.astral.vip\nGithub: https://github.com/foliclient/FoliClientInstaller')],
                                                                    [sg.Frame('Install Directory', layout=[[sg.InputText(key='inputpath', expand_x=True), sg.FolderBrowse(key='browsepath')]], tooltip='The directory where Foli Client should be installed', expand_x=True)],
                                                                    [sg.B('Continue'), sg.B('Exit')]]).read(close=True)
    if event == sg.WIN_CLOSED or event == 'Exit':
        sys.exit(0)
    elif event == 'Continue':
        if values['inputpath']:
            destpath = values['inputpath']
        else:
            destpath = values['browsepath']
        message_log('Recieved \"{destpath}\" from window.')

# Validates that the installation path is valid
isdir = os.path.isdir(destpath)
if not isdir:
    error_popup(f'Uh oh, \"{destpath}\" is not a folder on your computer! Please check for any typos!')
else:
    message_log(f'\"{destpath}\" is a valid directory')

    # Prompts user to confirm install directory
    event, values = sg.Window('Confirm Install Directory', [[sg.T(f'Are you sure you want to install Foli Client to \"{destpath}\"?')], [sg.B('Yes'), sg.B('No')]], disable_close=True).read(close=True)
    if event == sg.WIN_CLOSED or event == 'No':
        exit_popup()
    else:
        message_log('Directory confirmed by user')

# Asks the user if they want to use Optifine
if (not args.optifine and not args.sodium and not args.iris):
        event, values = sg.Window('Select a Graphics Mod', [[sg.T(f'Please select which graphics mod to install:')], 
                                                            [sg.Radio('Sodium w/ Extras (Recommended)', "GMODS", default=True, key='use_sodium')],
                                                            [sg.Radio('Sodium w/ Iris (Recommended for shader users)', "GMODS", key='use_iris')],
                                                            [sg.Radio('Optifine (Not Recommended)', "GMODS", key='use_optifine')],
                                                            [sg.B('Continue'), sg.B('Exit')]], disable_close=True).read(close=True)
        if event == sg.WIN_CLOSED or event == 'Exit':
            exit_popup()
        elif event == 'Continue':
            if values['use_optifine']:
                message_log('Optifine Selected')
                use_optifine = True
                use_iris = False
            elif values['use_iris']:
                message_log('Iris Selected')
                use_optifine = False
                use_iris = True
            else:
                message_log('Sodium Selected')
                use_optifine = False
                use_iris = False
if use_optifine:
    graphics_selection_string = 'Optifine'
elif use_iris:
    graphics_selection_string = 'Sodium w/ Iris'
else:
    graphics_selection_string = 'Sodium w/ Extras'

# Confirm install details and warn about file write
# Prompts user to confirm install directory
event, values = sg.Window('Confirm Install Details', [[sg.T(f'Your Selections:\nDestination Folder: \"{destpath}\"\nGraphics Mod: \"{graphics_selection_string}\"')], [sg.Text('Would you like to proceed with the install? This will write files to the selected folder.')], [sg.B('Yes'), sg.B('No')]], disable_close=True).read(close=True)
if event == sg.WIN_CLOSED or event == 'No':
    exit_popup()
else:
    message_log('Install confirmed by user')

# Validates and copies files
commonpath = get_full_path(os.path.join('resources', 'common'))
copydir(commonpath, destpath)
if(use_optifine):
    optifinepath = get_full_path(os.path.join('resources', 'optifine'))
    copydir(optifinepath, destpath)
elif(use_iris):
    irispath = get_full_path(os.path.join('resources', 'iris'))
    copydir(irispath, destpath)
else:
    sodiumpath = get_full_path(os.path.join('resources', 'sodium'))
    copydir(sodiumpath, destpath)
        

# Astral wooooooo
if args.astral:
    custom_log('MESSAGE', 'WAKE THE FUCK UP ASTRAL WE\'RE GOING TO THE FUCKING STARS WOOOOOOOOOOOOOOOO')
    os.rename(destpath + os.sep + 'config' + os.sep + 'bg.jpg', destpath + os.sep + 'config' + os.sep + 'bgoriginal.jpg')
    os.rename(destpath + os.sep + 'config' + os.sep + 'astral.jpg', destpath + os.sep + 'config' + os.sep + 'bg.jpg')

# Success Message
message_log('Install Completed')
sg.Window('Installation Completed', [[sg.T('Thank you for installing Foli Client! Please make sure to enable the texturepacks once installed')], [sg.Exit()]], disable_close=True).read(close=True)
