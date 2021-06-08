## -----------------------------------------------------------------------------
## Python Scripts                                       scriptarium/[loadzip.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import os
import re
import sys
from zipfile import ZipFile

from constants import zip_ignore
from functions import list_files

# os.chdir('X:\\test') # <- only uncomment for debugging
cwd = os.getcwd()

# read tag from arguments
tag = ''
if len(sys.argv) == 2:
    tag = sys.argv[1].strip()
    if re.match('^[A-Z_a-z0-9]*$', tag) == None:
        print('bad tag:', tag)
        quit()
    if len(tag) > 0:
        tag = '-' + tag
elif len(sys.argv) > 2:
    print('too many arguments')
    quit()

# locate the most recent zip file
zip_dir, zip_name, max_time = 'Z:\\', '', ''
folder = os.path.basename(cwd)
pat = re.compile('.*-' + folder + tag + '.*\.zip$')
for fname in os.listdir(zip_dir):
    path = os.path.join(zip_dir, fname)
    if os.path.isfile(path) and pat.match(fname) != None:
        tm = fname[:fname.index('-' + folder)]
        if tm > max_time:
            zip_name, max_time = path, tm
if zip_name == '':
    print('not found')
    quit()

# get list of files to extract
zip = ZipFile(zip_name, 'r')
zfiles = []
for fl in zip.filelist:
    s = fl.filename.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        continue
    if fl.filename[:5] != '.git/':
        zfiles.append(fl.filename)

# update changed files
for fname in zfiles:
    path = os.path.join(cwd, fname)
    if os.path.exists(path):
        zb = zip.read(fname)
        fb = open(path, 'rb').read()
        a = len(zb)
        b = len(fb)
        if zb == fb:
            continue
        zip.extract(fname)
        print('*', fname)

# add new files
for fname in zfiles:
    path = os.path.join(cwd, fname)
    if not os.path.exists(path):
        zip.extract(fname)
        print('+', fname)

# delete extra files in folder
for fname in list_files(cwd):
    if fname.find('.git\\') != -1 or fname.find('.git/') != -1:
        continue
    fname = fname.replace(cwd, '').lstrip('/\\').replace('\\', '/')
    s = fname.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        print('ignored ->', fname)
        continue
    if not fname in zfiles:
        os.remove(os.path.join(cwd, fname))
        print('-', fname)

zip.close()
print('\n' + 'loaded ' + zip_name + '\n')
quit()

# end
