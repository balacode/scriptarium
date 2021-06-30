## -----------------------------------------------------------------------------
## Python Scripts                                            scriptarium/[td.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

import re, sys
from datetime import date, datetime, timedelta

DATETIME  = r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d'
DATETIME2 = r'\d\d\d\d-\d\d-\d\d \d\d:\d\d'
TIME      = r'\d\d:\d\d:\d\d'
TIME2     = r'\d\d:\d\d'

def to_datetime(s):
    if re.match(DATETIME, s) != None:
        s = s
    elif re.match(DATETIME2, s) != None:
        s = s + ':00'
    elif re.match(TIME, s) != None:
        s = str(date.today()) + ' ' + s
    elif re.match(TIME2, s) != None:
        s = str(date.today()) + ' ' + s + ':00'
    return datetime.fromisoformat(s)

args  = ' '.join(sys.argv[1:])
times = []
for i in range(2):
    for expr in [DATETIME, DATETIME2, TIME, TIME2]:
        m = re.search(expr, args)
        if m != None:
            i, j = m.regs[0][0], m.regs[0][1]
            s = args[i:j]
            times.append(to_datetime(s))
            args = args[j:]
            break

if len(times) == 2:
    td: timedelta = (times[1] - times[0])
    min = td / timedelta(minutes=1)
    min = '(' + str(min) + ' m)'
    min = min.replace('.0 ', ' ')
    print(str(td), min)
else:
    print('#error')

# end
