# ------------------------------------------------------------------------------
# Python Scripts                              scriptarium/[remove_empty_dirs.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import os
import sys

# process command-line arguments
root = old_cwd = os.getcwd()
verbose = False
if len(sys.argv) > 3: # program name + 2 arguments
    print('too many arguments')
    quit()
for arg in sys.argv[1:]:
    if arg.lower() == "--verbose" or arg.lower() == "-verbose":
        verbose = True
    else:
        root = arg

dirs = list(os.walk(root, topdown = False))
for dir in dirs:

    # obtain folder's path and list of files and folders
    path = dir[0]
    if path == root:
        continue
    os.chdir(path)

    # remove .DS_Store MacOS files
    files = dir[2]
    if len(files) == 1:
        name = files[0]
        if name == ".DS_Store":
            os.remove(name)
            if verbose:
                print('deleted file "'+name+'"')
            files = []

    # get folder contents after child folders/files were possibly removed
    contents = os.listdir()

    # remove empty folder and continue
    if len(contents) == 0:
        os.rmdir(path)
        if verbose:
            print('deleted dir "'+path+'"')
        continue

    # if folder is not empty, display number of subfolders and files it contains
    if verbose:
        n_dirs, n_files = 0, 0
        for s in contents:
            if os.path.isdir(s):
                n_dirs += 1
            else:
                n_files += 1
        print('retained dir "'+path+'" has', n_dirs, 'dir(s),', n_files, 'file(s)')
        continue

os.chdir(old_cwd)
quit()

# end
