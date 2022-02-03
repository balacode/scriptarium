# ------------------------------------------------------------------------------
# Python Scripts                                        scriptarium/[savezip.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import os
import platform
import re
import sys

from datetime import datetime
from zipfile import ZipFile

from constants import zip_ignore
from functions import format_size, list_files

# set the location where zip files are saved
ps = platform.system()
if ps == 'Linux' or ps == 'Darwin':
    zip_dir = '/x/user/zip'
elif ps == 'Windows':
    zip_dir = 'Z:\\user\\zip'
else:
    print('unknown os:', ps)
    quit()

# read tag from arguments
tag = ''
if len(sys.argv) == 2:
    tag = sys.argv[1].strip()
    if re.match('^[A-Z_a-z0-9]*$', tag) == None:
        print('bad tag:', tag)
        quit()
    else:
        tag = '-' + tag
elif len(sys.argv) > 2:
    print('too many arguments')
    quit()

# only uncomment for debugging:
# os.chdir('/x/user/scripts/scriptarium')
# os.chdir('X:\\user\\scripts\\scriptarium')
cwd = os.getcwd()

# create the zip file, named with the current time and folder name
zip_name = os.path.join(zip_dir, \
            datetime.today().strftime('%Y-%m-%d-%H%M%S-') + \
            os.path.basename(cwd) + \
            tag + \
            '.zip')
zip = ZipFile(zip_name, 'w')

# store all matching files in the archive
file_count = 0
for name in list_files('.'):

    size = os.path.getsize(name)
    if name[:2] == '.\\' or name[:2] == './':
        name = name[2:]    
    
    # skip file names that match entries in zip_ignore 
    s = name.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        print('ignored ->', name, '(' + format_size(size) + ')')
        continue

    # skip likely executable/binary files (files without a file
    # extension, larger than 1MB, and not in the .git folder)
    if not '.' in name and size > 1024*1024 and not '.git' in name:
        print('ignored ->', name, '(' + format_size(size) + ')')
        continue

    # write the file
    zip.write(name)
    file_count += 1

# save the zip
zip.close()
if os.path.exists(zip_name):
    size = format_size(os.path.getsize(zip_name))
    print('\n' + 'saved ' + zip_name + ': ' + size + ',', file_count, 'files\n')
quit()

# end
