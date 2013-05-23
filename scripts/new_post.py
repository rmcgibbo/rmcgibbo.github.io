from __future__ import print_function
import os
import sys
import datetime

if len(sys.argv) == 2:
    title = sys.argv[1]
else:
    title = raw_input('title: ')

now = datetime.datetime.now()
date_string = datetime.datetime.strftime(now, '%Y-%m-%d')
datettime_string = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M')
lower_title = title.replace(' ', '-').lower()
filename = 'content/%s-%s.md' % (date_string, lower_title)

if os.path.exists(filename):
    print('%s already exists' % lower_title)
    sys.exit(1)

with open(filename, 'w') as f:
    print('creating %s' % filename)

    f.write('Title: %s\n' % title)
    f.write('date: %s\n' % datettime_string)
    f.write('comments: true\n')
    f.write('slug: %s\n\n' % title)

