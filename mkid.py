## -----------------------------------------------------------------------------
## Python Scripts                                          scriptarium/[mkid.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import os
import re
import secrets
import sys

from constants import text_file_exts
from functions import list_files

# os.chdir('X:\\test') # <- only uncomment for debugging
cwd = os.getcwd()

# duplicate IDs to ignore (specify hex digits in upper case)
ignore_ids = [
    'E12345'
]

# create dictionary of 6-digit IDs by reading files
# in the current folder and its subfolders
ids6 = {}
id_rx = re.compile('E[0-9a-fA-F]+')
for filename in list_files('.'):
    # skip file types not listed in text_file_exts
    if not next(
        (ext for ext in text_file_exts if filename.endswith(ext)), False
    ):
        continue
    #
    with open(filename, mode='r', encoding='utf-8') as fl:
        for id in fl.read().split('0x'):
            id = id[:6].upper()
            match = id_rx.match(id)
            if match == None:
                continue
            id = id[:match.regs[0][1]]
            if id in ignore_ids:
                continue
            if id in ids6:
                ids6[id] += 1
            else:
                ids6[id] = 1

# create dictionary of 4-digit IDs from 6-digit IDs, ignoring the first 'E'
ids4 = {}
for id in ids6:
    for s in [id[1:5], id[2:6]]:
        if len(s) < 1:
            continue
        if s in ids4:
            ids4[s] += 1
        else:
            ids4[s] = 1

# print all non-unique 6-digit IDs:
if True:
    title = True
    for k, v in ids6.items():
        k = '0x' + k
        if v > 1:
            if title:
                print('\n' + 'non-unique ids (6-digit):')
                title = False
            print(k + ': ' + str(v))

# print all non-unique 4-digit IDs:
if True:
    title = True
    for k, v in ids4.items():
        if v > 1:
            if title:
                print('\n' + 'non-unique ids (4-digit):')
                title = False
            print(k + ': ' + str(v))

# create new unique ID(s)
print('\n' + 'new unique ID:')
count = 1
if len(sys.argv) > 1:
    count = int(sys.argv[1])
while count > 0:
    id = 'E' + secrets.token_hex(3)[:5].upper()
    if re.match(r'.*\d\d\d.*', id) != None:
        continue
    if re.match(r'.*[A-Z]{4}.*', id) != None:
        continue
    found = False
    for s in [id[0: 4], id[1: 5], id[2: 6]]:
        if s in ids4:
            found = True
            break
    if found:
        continue
    for s in [id[0: 4], id[1: 5], id[2: 6]]:
        ids4[s] = 1
    print('0x' + id)
    count -= 1
    continue

print()

# end
