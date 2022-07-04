# ------------------------------------------------------------------------------
# Python Scripts                                     scriptarium/[list-words.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

# list-words lists the words in every text file
# in the current folder and its subfolders.

import re

from typing import List

from sys import argv as sys_argv

from constants import text_file_exts
from functions import list_files

def split_words(s: str) -> List[str]:
    mode = ''
    ar = []
    w = ''
    for c in s:
        if c.isupper():
            if mode == 'l' or mode == 'd':
                ar.append(w)
                w = c
            else:
                w += c
            mode = 'u'

        elif c.islower():
            mode = 'l'
            w += c

        elif c.isdigit():
            mode = 'd'
            w += c

        else:
            mode = ''
            if w != '':
                ar.append(w)
                w = ''

    if w != '':
        ar.append(w)

    return ar

def test_split_words():
    test_cases = [
        ['Hello', ['Hello']],
        ['HelloWorld', ['Hello', 'World']],
        ['helloWorld', ['hello', 'World']],
        ['yard_number', ['yard', 'number']],
    ]
    for tc in test_cases:
        input = tc[0]
        want = tc[1]
        have = split_words(input)
        if have != want:
            print('ok')
            raise Exception(f'words(\'{input}\') -> {have} expected: {want}')

test_split_words()

#-------------------------------------------------------------------------------

print('\n'*10)

dictionary = {}
if len(sys_argv) > 1:
    for fname in sys_argv:
        if fname == sys_argv[0]:
            continue
        with open(fname, mode='r', encoding='utf-8') as fl:
            for s in fl.read().splitlines():
                i = s.find('#')
                if i != -1:
                    s = s[:i]
                s = s.strip()
                if s != '':
                    if s in dictionary:
                        print('duplicate:', s)
                    else:
                        dictionary[s] = True
                    u = s.upper()
                    if u != s:
                        if u in dictionary:
                            print('duplicate:', u)
                        else:
                            dictionary[u] = True
    print('loaded dictionary')

for fname in list_files('.'):

    # skip file types not listed in text_file_exts
    if not next((ext for ext in text_file_exts if fname.endswith(ext)), False):
        continue

    print('\n'*2 + '-'*80 + '\n' + fname)
    words = []
    ln = ''

    with open(fname, mode='r', encoding='utf-8') as fl:
        s = fl.read()
        ln = ''

        for c in s:
            if (c == '_') \
            or (c >= '0' and c <= '9') \
            or (c >= 'a' and c <= 'z') \
            or (c >= 'A' and c <= 'Z'):
                ln += c
                continue
            if ln != '' and not ln in words:
                words.append(ln)
            ln = ''

        if ln != '' and not ln in words:
            words.append(ln)

    words.sort()
    for ln in words:

        if ln == '':
            continue
        if ln[0].isdigit():
            continue
        if ln in dictionary:
            continue
        if ln[:1].lower()+ln[1:] in dictionary:
            continue

        allWordsInDict = True
        for w in split_words(ln):
            lw = w[:1].lower()+w[1:]
            if (w not in dictionary) and (lw not in dictionary):
                allWordsInDict = False
                break
        if allWordsInDict:
            continue

        print(ln)

quit()

# end
