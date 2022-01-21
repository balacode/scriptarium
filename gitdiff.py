# ------------------------------------------------------------------------------
# Python Scripts                                        scriptarium/[gitdiff.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import os
import subprocess
from functions import get_int
from functions import list_git_repos

# os.chdir('X:\\user\\projects\\code\\go\\src\\base')
cwd = os.getcwd()

repos = list_git_repos(cwd)
for path in repos:
    path = str(path)
    os.chdir(path)

    got = str(subprocess.run(['git', 'diff', '--compact-summary'], \
        capture_output=True, \
        encoding='utf8').stdout)

    for ln in got.split('\n'):

        if ln.find('files changed') >= 0 and \
        ln.find('insertions') >= 0 and \
        ln.find('deletions') >= 0:

            # 0 files changed, 0 insertions(+), 0 deletions(-)
            p = ln.split(',')
            f = (str(get_int(p[0])) + 'f').ljust(5, ' ')
            i = ('+' + str(get_int(p[1]))).ljust(5, ' ')
            d = ('-' + str(get_int(p[2]))).ljust(5, ' ')
            path = path.replace(cwd, '')
            if len(path) == 0:
                path = "."
            print(f, i, d, path)
            break

os.chdir(cwd)

# end
