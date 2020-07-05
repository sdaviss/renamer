# Renamer
License: MIT
Language: Python3
Author: Steven Daviss (c) 2020

Takes files in a directory named with unique text and renames and moves them based on a dictionary of key:value pairs. No frills, some reporting. I'm sure there must be tons of these written, but I'm using this to sharpen my #python and git skills. 

## Description
  * Rename files using a dictionary of oldnames:newnames, and moving them from a source dir to a target dir, and printing a list of moved files, as well as a list of unmodified files with problems.

## Features
  * the names of folders and files are inside the code
  * before a file in the destination directory is overwritten, it must be approved by the user
  * the number of files moved and renamed is indicated

## Output
```
#56.  Original file  /Users/lazaruslong/Screenshots/Screenshot 2020-06-26 14.45.56.png  changed to  /Users/lazaruslong/Automatic/Automatic-VW-2020-miles.png
#57.  Original file  /Users/lazaruslong/Screenshots/Screenshot 2020-06-26 14.47.51.png  changed to  /Users/lazaruslong/Automatic/Automatic-VW-20200220.png
#58.  Original file  /Users/lazaruslong/Screenshots/Screenshot 2020-06-26 14.48.21.png  changed to  /Users/lazaruslong/Automatic/Automatic-VW-20200221.png

==========  58 FILES RENAMED AND MOVED FROM  /Users/lazaruslong/Screenshots/
                                         TO  /Users/lazaruslong/Automatic/

==========  1 FILES IN SOURCE DIR THAT DID NOT EXIST
/Users/lazaruslong/Screenshots/Screenshot 2020-06-26 08.11.41.png
```

## Improvements to consider
  1. if newfile exists and user wants to proceed with overwriting it, then create a new folder inside the current one, and move the oldfile to this folder in case user still needs the old version.
  2. check for errors.
  3. change colors on ouput to group visually.
  4. add a log file to track datetimes and file change history
  
 
