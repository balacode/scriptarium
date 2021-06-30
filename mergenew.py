## -----------------------------------------------------------------------------
## Python Scripts                                      scriptarium/[mergenew.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import re

from constants import text_file_exts
from functions import list_files

for fname in list_files('.'):

    # skip file types not listed in text_file_exts
    if not next((ext for ext in text_file_exts if fname.endswith(ext)), False):
        continue

    with open(fname, mode='r', encoding='utf-8') as fl:

        # skip files that have no merge conflicts
        s = fl.read()
        if s.find('\n=======\n') < 0:
            continue

        # strip merge tags together with the old code, leaving new changes
        # (substitute '\0' for '\n' so that regex applies over entire file)
        s = s.replace('\n', '\0')
        s = re.sub('\0<<<<<<< HEAD.*?\0=======\0', '\0', s)
        s = re.sub('\0>>>>>>> .*?\0',              '\0', s)
        s = s.replace('\0', '\n')

    with open(fname, 'wb') as fl:
        n = fl.write(s.encode('utf8'))
        print('-->', fname)

# end
