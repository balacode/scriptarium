## -----------------------------------------------------------------------------
## Python Scripts                                       scriptarium/[savezip.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import os
import re
import sys
from datetime import datetime
from zipfile import ZipFile

from constants import zip_ignore
from functions import format_size, list_files

# os.chdir('X:\\test') # <- only uncomment for debugging
cwd = os.getcwd()

# read tag from arguments
tag = ''
if len(sys.argv) == 2:
    tag = sys.argv[1]
    if re.match('^[A-Z_a-z0-9]*$', tag) == None:
        print('bad tag:', tag)
        quit()
    else:
        tag = '-' + tag
elif len(sys.argv) > 2:
    print('too many arguments')
    quit()

# create the zip file, named with the current time and folder name
zip_name = 'Z:\\' + \
            datetime.today().strftime('%Y-%m-%d-%H%M%S-') + \
            os.path.basename(cwd) + \
            tag + \
            '.zip'
zip = ZipFile(zip_name, 'w')

# store all matching files in the archive
nfiles = 0
for name in list_files('.'):
    # skip file names that match entries in zip_ignore
    if name[:2] == '.\\' or name[:2] == './':
        name = name[2:]
    s = name.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        print('ignored ->', name)
    else:
        zip.write(name)
        nfiles += 1

zip.close()
if os.path.exists(zip_name):
    size = format_size(os.path.getsize(zip_name))
    print('\n' + 'saved ' + zip_name + ': ' + size + ',', nfiles, 'files\n')

quit()

# end
