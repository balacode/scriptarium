## -----------------------------------------------------------------------------
## Python Scripts                                        scriptarium/[fname2.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import os

os.chdir('T:\\eBooks') # <- only uncomment for debugging

sources = {}

with open("list1.txt", mode='r', encoding='ansi') as fl:
    lines = fl.read().split('\n')
    for ln in lines:
        if len(ln) < 34:
            continue
        id = ln[:32]
        s = ln[33:]
        sources[id] = s

with open("list2.txt", mode='r', encoding='ansi') as fl:
    lines = fl.read().split('\n')
    for ln in lines:
        if len(ln) < 34:
            continue
        ln = ln.strip()
        id = ln[:32].strip()
        new_name = ln[33:].strip()
        #
        if not id in sources:
            print("NO MATCH:", id, new_name)
            continue
        #
        path = sources[id]
        old_name = path
        j = path.rfind('\\')
        if j > -1:
            old_name = path[j+1:]
        #
        if new_name == old_name:
            continue
        #
        try:
            os.rename(path, new_name)
            print(path, "--->", new_name)
        except WindowsError:
            print("FAILED:", path, "--->", new_name)

# end
