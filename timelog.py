## -----------------------------------------------------------------------------
## Python Scripts                                       scriptarium/[timelog.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import re

def has_timestamp(s):
    return re.match(r'^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d.*', s) != None

fname = 'X:\\user\\admin\\timelog.txt'
lines = []
prev  = ''

with open(fname, mode='r', encoding='utf-8') as fl:
    for ln in fl.read().split('\n'):
        if has_timestamp(ln):

            # mark times that are the same
            # a = ln[:19]
            # b = prev[:19]
            # if a == b:
            #     lines.append(ln + ' ``')
            #     prev = ln
            #     continue

            # mark descriptions that are the same
            a = ln[19:]
            b = prev[19:]
            if a == b:
                if prev.find(':00 ') > 0:
                    lines[len(lines)-1] = '````'

                # if prev.find(':00 ') > 0:
                #     lines[len(lines)-1] = prev + ' ``'
                # else:
                #     lines.append(ln + ' ``')
                #     prev = ln
                #     continue

            prev = ln
        lines.append(ln)

with open(fname, 'wb') as fl:
    s = '\n'.join(lines)
    fl.write(s.encode('utf8'))

# end
