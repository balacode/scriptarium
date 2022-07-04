# ------------------------------------------------------------------------------
# Python Scripts                            scriptarium/[timelog_check_times.py]
# (c) balarabe@protonmail.com
# ------------------------------------------------------------------------------

import re
import sys

from datetime import date, datetime, timedelta

file_name = 'timelog.txt'
if len(sys.argv) == 2:
    file_name = sys.argv[1].strip()

def get_tag(s):
    if ': ' in s:
        i = s.index(': ')
        s = s[:i]
    if has_timestamp(s):
        s = s[19:].strip()
    return s

def diff_minutes(iso1, iso2):
    def to_datetime(s):
        if re.match(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', s) != None:
            s = s[:19]
        elif re.match(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d', s) != None:
            s = s[16:] + ':00'
        elif re.match(r'\d\d:\d\d:\d\d', s) != None:
            s = str(date.today()) + ' ' + s
        elif re.match(r'\d\d:\d\d', s) != None:
            s = str(date.today()) + ' ' + s + ':00'
        return datetime.fromisoformat(s)
    td: timedelta = (to_datetime(iso2) - to_datetime(iso1))
    m = td / timedelta(minutes=1)
    return m

def has_timestamp(s):
    return re.match(r'^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d.*', s) != None

def next_second(iso):
    tm = datetime.fromisoformat(iso[:19])
    tm += timedelta(seconds=1)
    return tm.isoformat().replace('T', ' ')

def prev_second(iso):
    tm = datetime.fromisoformat(iso)
    tm -= timedelta(seconds=1)
    return tm.isoformat().replace('T', ' ')

old_lines, new_lines, prev_line, prev_tag = [], [], '', ''

with open(file_name, mode='r', encoding='utf-8') as fl:
    old_lines = fl.read().split('\n')

for line in old_lines:
    line = line.strip()
    t1, d1, t2, d2 = prev_line[:19], prev_line[19:], line[:19], line[19:]

    # ignore lines without timestamps
    if not has_timestamp(line):
        new_lines.append(line)
        continue

    # mark lines with duplicate timestamps
    elif t1 == t2:
        new_lines.append('<<<< DUPLICATE_TIME')

    # mark lines with duplicate descriptions
    elif d1 == d2:
        new_lines.append('<<<< DUPLICATE_NOTE')

    # insert missing times
    elif has_timestamp(prev_line):
        tag = get_tag(line)
        if tag != prev_tag and not (': IN ' in line or line.endswith(': IN')):
            m = diff_minutes(prev_line, line)
            if m <= 15:
                s = next_second(prev_line[:19]) + ' ' + tag + ': IN'
            else:
                s = prev_second(line[:19]) + ' ' + tag + ': IN <<<<'
            new_lines.append(s)

    new_lines.append(line)
    prev_line = line
    prev_tag  = get_tag(line)

with open(file_name, 'wb') as file:
    s = '\n'.join(new_lines)
    file.write(s.encode('utf8'))

# end
