#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:00:35 2020
@author: Steven Daviss (sdaviss)
#####  Rename files using a dictionary of oldnames:newnames, 
#####  and moving them from a source dir to a target dir, and printing a list of
#####  moved files, as well as unmodified files with problems.

"""

import os

##### CHANGE SOURCE/OLD and DEST/NEW FOLDER LOCATIONS, NON-UNIQUE     #####
#####    FILENAME PORTIONS, and EXTENSIONS BELOW                      #####
oldpathto = '/Users/lazaruslong/Screenshots/'
oldprefix = 'Screenshot 2020-06-26 '
newpathto = '/Users/lazaruslong/Automatic/'
newprefix = 'Automatic-'
ext = '.png'                                        # presumes extension does not change


##### THIS IS WHERE THE UNIQUE PORTIONS OF THE FILENAMES ARE INSERTED #####
filedict = {                                        # INSERT dictionary of old filenames (key) and new target filenames (value)
    'oldname': 'newname'
    }                                                                 #####
##### e.g., '07.42.39': '202003',                                     #####


##### VARIABLES USED TO TRACK FILES
notExistOld = []                                    # list of original files in source dir that did not exist
notChangedOld = []                                  # list of original files in source dir that were NOT moved to target dir
preexistNewStop = []                                # list of original TARGET files that were already in target dir and were NOT overwritten
preexistNewGo = []                                  # list of TARGET files in target dir that WERE overwritten by request
movedfiles = 0                                      # counter for # of files that were moved


##### LOGIC AND SCREEN NOTIFICATIONS OF PROGRESS
print('\n')
for x, y in filedict.items():                       # Go thru the list of files
    oldpathfile = oldpathto + oldprefix + x + ext
    newpathfile = newpathto + newprefix + y + ext
    if os.path.exists(oldpathfile):                 # Old exists - keep going
        if os.path.exists(newpathfile):             # New exists - ask user to proceed w/overwriting current file
            continuenew = input('WARNING!  ' + newpathfile + '  exists and will be overwritten. Enter Y to proceed, any other key to skip:  ')
            print('\n')
            if continuenew.lower() == 'y' :         # User says to overwrite existing file in target dir
                os.rename(oldpathfile, newpathfile)
                movedfiles = movedfiles + 1
                print('#'+str(movedfiles)+'.', ' User chose to overwrite target file (', newpathfile, ') with original ', oldpathfile)
                print('\n')
                preexistNewGo.append(newpathfile)
                continue
            else:                                   # User says to keep existing file in target dir
                preexistNewStop.append(newpathfile)
                notChangedOld.append(oldpathfile)
                continue
        else:                                       # New does NOT exist - proceed with renaming old to new
            os.rename(oldpathfile, newpathfile)
            movedfiles = movedfiles + 1
            print('#'+str(movedfiles)+'.', ' Original file ', oldpathfile, ' changed to ', newpathfile)
            print('\n')
            continue
    else:                                           # Old does NOT exist - cannot proceed on this file
        notExistOld.append(oldpathfile)
        continue


##### SUMMARY OF WHAT HAPPENED AND ALERTS ABOUT UNEXPECTED FINDINGS
print('========== ', movedfiles, 'FILES RENAMED AND MOVED FROM ', oldpathto) 
print('                                        TO ', newpathto)
print('\n')

if len(notExistOld) > 0:
    print('========== ', len(notExistOld), 'FILES IN SOURCE DIR THAT DID NOT EXIST')
    for x in notExistOld:
        print(x)
    print('\n')

if len(notChangedOld) > 0:
    print('========== ', len(notChangedOld), 'FILES IN SOURCE DIR THAT WERE *NOT* MOVED TO TARGET DIR')
    for x in notChangedOld:
        print(x)
    print('\n')

if len(preexistNewGo) > 0:
    print('========== ', len(preexistNewGo), "EXISTING FILES IN TARGET DIR OVERWRITTEN AT USER'S REQUEST")
    for x in preexistNewGo:
        print(x)
    print('\n')

if len(preexistNewStop) > 0:
    print('========== ', len(preexistNewStop), "EXISTING FILES IN TARGET DIR *NOT* OVERWRITTEN AT USER'S REQUEST")
    for x in preexistNewStop:
        print(x)
    print('\n')


##### future -- if newfile exists and user wants to proceed, then move the existing file to a new folder in case user still needs the old version

##### /end
        
          
