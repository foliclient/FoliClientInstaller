import sys
import os
import shutil
import PySimpleGUI as sg

version = '2.1.0'

# ------------------------------------------------------------ #

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

def copydir(sourcedir, destdir, destpath, verbose):
    # Walks the given folder and copies all files and subdirectories to the destination
    for subdir, dirs, files in os.walk(sourcedir):
        for filename in files:
            filepath = subdir + os.sep + filename
            destination = subdir.replace(sourcedir, '')
            os.makedirs(destdir + destination, exist_ok=True)
            fulldestpath = destpath + destination + os.sep + filename
            shutil.copyfile(filepath, fulldestpath)
            if(verbose):
                print(f'[LOG]\tCopied {destination + os.sep + filename} to {fulldestpath}')

# ------------------------------------------------------------ #

def install():
    

# ------------------------------------------------------------ #

def main():
    sg.theme('Dark')  # please make your windows colorful

    duringinstall = False

    layout = [[sg.Text('Welcome to the Foli Client Installer! Please read the instructions on the website before installing!')],
            [sg.Text('Install Directory'), sg.InputText(disabled=duringinstall), sg.FolderBrowse(disabled=duringinstall)],
            [],
            [sg.Text('Graphics Mods:')],
            [sg.Radio('Sodium w/ Extras (Recommended)', "GMODS", default=True, disabled=duringinstall)],
            [sg.Radio('Sodium w/ Iris (Recommended for shader users)', "GMODS", disabled=duringinstall)],
            [sg.Radio('Optifine (Not Recommended)', "GMODS", disabled=duringinstall)],
            [],
            [sg.Checkbox('Verbose Mode', disabled=duringinstall)],
            [sg.Text('Install Log', visible=duringinstall)],
            [sg.Output(visible=duringinstall)],
            [sg.Button('Install'), sg.Button('Website'), sg.Button('Exit', disabled=duringinstall)]]

    window = sg.Window(f'Foli Client Installer v{version}', layout)

    while True:  # Event Loop
        event, values = window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Install':
            # change the "output" element to be the value of "input" element
            duringinstall = True
            print("boop")
            event, values = window.read()

    window.close()

# ------------------------------------------------------------ #

if __name__ == "__main__":
    main()