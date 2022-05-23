# ------------------------------------------------------------------------------
# Python Scripts                                     scriptarium/[list-words.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

# list-words lists the words in every text file
# in the current folder and its subfolders.

import re

from constants import text_file_exts
from functions import list_files

print('\n'*10)

def process_word():
    if not word in words:
        words.append(word)

for fname in list_files('.'):

    # skip file types not listed in text_file_exts
    if not next((ext for ext in text_file_exts if fname.endswith(ext)), False):
        continue

    print('\n'*2 + '-'*80 + '\n' + fname)
    words = []
    word = ''

    with open(fname, mode='r', encoding='utf-8') as fl:
        s = fl.read()
        word = ''

        for c in s:
            if (c == '_') \
            or (c >= '0' and c <= '9') \
            or (c >= 'a' and c <= 'z') \
            or (c >= 'A' and c <= 'Z'):
                word += c
                continue
            if word != '':
                process_word()
            word = ''

        if word != '':
            process_word()

    words.sort()
    for word in words:
        print(word)

quit()

# end
