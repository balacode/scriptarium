## -----------------------------------------------------------------------------
## Python Scripts                                     scriptarium/[functions.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import os
import re

# describes a file size as a human-friendly value
def format_size(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti']:
        if abs(num) < 1024.0:
            return '%3.1f%s%s' % (num, unit, suffix)
        num /= 1024.0
    return '%.1f%s%s' % (num, 'Pi', suffix)

# returns the first integer from a given string
def get_int(s):
    m = re.search(r'\d+', s)
    if m == None:
        return 0
    return int(m.group())

# lists all files in 'dir' and its subfolders
def list_files(dir):
    ret = []
    for fname in os.listdir(dir):
        path = os.path.join(dir, fname)
        if os.path.isdir(path):
            ret += list_files(path)
        else:
            ret.append(path)
    return ret

# lists all paths within directory 'dir' that contain Git repositories
def list_git_repos(dir):
    ret = []
    for fname in os.listdir(dir):
        if fname == '.git':
            ret.append(dir)
        else:
            path = os.path.join(dir, fname)
            if os.path.isdir(path):
                ret += list_git_repos(path)
    return ret

# end
