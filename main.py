import sys
import os
import shutil

if len(sys.argv) > 2:
    print('[ERROR]\tUh oh, there seems to be too many command arguments! If you\'ve only put in your minecraft directory as an argument, try wrapping it in quotes!')
    print('\nPress any key to exit...')
    input()
    sys.exit()

destPath = ''

if len(sys.argv) == 2:
    destpath = sys.argv[1]
else:
    print('[INPUT]\tPlease type in the full filepath of your .minecraft folder:')
    destpath = input()

isdir = os.path.isdir(destpath)

if not isdir:
    print('[ERROR]\tUh oh, that\'s not a folder! Please check for any typos!')
    print('\nPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\t' + destpath + ' is a valid directory')

sourcepath = os.path.dirname(__file__) + '\\resources'

if not os.path.isdir(sourcepath):
    print('[ERROR]\tCan\'t find the resources folder. Please re-download the package or make sure the resources folder is in the same directory as the python script')
    print('\nPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\tValidated resource directory')

print('\n')

for subdir, dirs, files in os.walk(sourcepath):
    for filename in files:
        filepath = subdir + os.sep + filename
        destination = subdir.replace(sourcepath, '')
        os.makedirs(destpath + destination, exist_ok=True)
        fulldestpath = destpath + destination + os.sep + filename
        shutil.copyfile(filepath, fulldestpath)
        print(f'[LOG]\tCopied {filepath} to {fulldestpath}')

print('\nAll files should have been copied over. Thanks for using Foli Client!')
print('\nPress any key to exit...')
input()
sys.exit()