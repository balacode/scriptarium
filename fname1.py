# ------------------------------------------------------------------------------
# Python Scripts                                         scriptarium/[fname1.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import os, binascii

os.chdir('T:\\eBooks') # <- only uncomment for debugging

lines1 = []
lines2 = []

with open("list.txt", mode='r', encoding='ansi') as fl:
    data = fl.read()
    src_lines = data.split('\n')
    for ln in src_lines:
        if ln == "" or (ln.find('.epub') == -1 and ln.find('.mobi') == -1):
            continue
        id = str(binascii.b2a_hex(os.urandom(16)))[2:34]
        #
        s = id + ' ' + ln
        lines1.append(s)
        #
        j = ln.rfind('\\')
        if j > -1:
            ln = ln[j+1:]
        s = id + ' ' + ln
        lines2.append(s)

with open("list1.txt", 'wb') as fl:
    s = '\n'.join(lines1) + '\n'
    fl.write(s.encode('utf8'))

with open("list2.txt", 'wb') as fl:
    s = '\n'.join(lines2) + '\n'
    fl.write(s.encode('utf8'))

# end
