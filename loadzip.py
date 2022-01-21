# ------------------------------------------------------------------------------
# Python Scripts                                        scriptarium/[loadzip.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import os
import platform
import re
import sys

from zipfile import ZipFile

from constants import zip_ignore
from functions import list_files

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
    if len(tag) > 0:
        tag = '-' + tag
elif len(sys.argv) > 2:
    print('too many arguments')
    quit()

# only uncomment for debugging:
# os.chdir('/x/user/scripts/scriptarium')
# os.chdir('X:\\user\\scripts\\scriptarium')
cwd = os.getcwd()

# locate the most recent zip file
zip_name, max_time = '', ''
folder = os.path.basename(cwd)
pat = re.compile('.*-' + folder + tag + '.*\.zip$')
for filename in os.listdir(zip_dir):
    path = os.path.join(zip_dir, filename)
    if os.path.isfile(path) and pat.match(filename) != None:
        tm = filename[:filename.index('-' + folder)]
        if tm > max_time:
            zip_name, max_time = path, tm
if zip_name == '':
    print('not found')
    quit()

# get list of files to extract
zip = ZipFile(zip_name, 'r')
zip_files = []
for fl in zip.filelist:
    s = fl.filename.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        continue
    if fl.filename[:5] != '.git/':
        zip_files.append(fl.filename)

# update changed files
for filename in zip_files:
    path = os.path.join(cwd, filename)
    if os.path.exists(path):
        zb = zip.read(filename)
        fb = open(path, 'rb').read()
        a = len(zb)
        b = len(fb)
        if zb == fb:
            continue
        zip.extract(filename)
        print('*', filename)

# add new files
for filename in zip_files:
    path = os.path.join(cwd, filename)
    if not os.path.exists(path):
        zip.extract(filename)
        print('+', filename)

# delete extra files in folder
for filename in list_files(cwd):
    if filename.find('.git\\') != -1 or filename.find('.git/') != -1:
        continue
    filename = filename.replace(cwd, '').lstrip('/\\').replace('\\', '/')
    s = filename.lower()
    if next((pat for pat in zip_ignore if re.match(pat, s)), False):
        print('ignored ->', filename)
        continue
    if not filename in zip_files:
        os.remove(os.path.join(cwd, filename))
        print('-', filename)

zip.close()
print('\n' + 'loaded ' + zip_name + '\n')
quit()

# end
