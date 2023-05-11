#!/usr/bin/env python3

method = '''
xprop -root
look for 
_NET_ACTIVE_WINDOW(WINDOW): window id # 0x1c00003

xprop -id 0x1c00003
look for:
WM_NAME(STRING) = "dtweed@teapot: ~/Dropbox/config/i3"

regex: 
m = re.search('WM_NAME\(STRING\) = "([^"]*)"'
WM_NAME\(STRING\) = "([^"]*)"

'''


import re
import subprocess

raw_xprop_string = subprocess.run(['xprop', '-root'], stdout=subprocess.PIPE)
#print(raw_name_string, "\n\n")

raw_xprop = raw_xprop_string.stdout.decode('utf-8')
# print(raw_name)

m = re.search('_NET_ACTIVE_WINDOW.* ([\w]+)', raw_xprop)
window_id = m.group(1)

# print(window_id)

raw_windowname = subprocess.run(['xprop', '-id', window_id ], stdout=subprocess.PIPE)
raw_windowname_string = raw_windowname.stdout.decode('utf-8')
# print(raw_windowname_string)

q = re.search('WM_NAME\([^"]*\) = "([^"]*)"', raw_windowname_string)
#print(q.group(1))
window_name = q.group(1)

print(window_name)
