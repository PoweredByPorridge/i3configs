#!/usr/bin/env python3

import re
import time
import subprocess

# # open temp file for appending, just to make sure it is there
# # then close it again
# f = open('/tmp/prev_stats_file', 'a')
# f.close()

# time is UNIX time, a number. Easier on the system, and
# as I'm not actually interested in it, we'll stick with
# it
cur_time = int(time.time())

raw = subprocess.run(['/bin/ip', 'route'], stdout=subprocess.PIPE)
ip_raw = raw.stdout.decode('utf-8')

m = re.search('^(?:\S+ ){4}(\S+)', ip_raw)
instance = m.group(1)

open_rx_string = '/sys/class/net/' + instance + '/statistics/rx_bytes'
open_tx_string = '/sys/class/net/' + instance + '/statistics/tx_bytes'
# print(open_string)

# read rx and tx bytes
# No longer assumes that the interface is eth0
with open(open_rx_string, 'r') as f:
    cur_rx = int(f.read())
    # print('current_rx: ', cur_rx, type(cur_rx))
with open(open_tx_string, 'r') as f:
    cur_tx = int(f.read())

# opens a file fo reading - assumes it exists
# could open as a+ earlier and add two numbers
# to create it
# Rewind, read in the values from the previous run
# and then close the file
with open('/tmp/prev_stats_file', 'r') as f:
    f.seek(0) 
    prev_rx, prev_tx, prev_time = f.readlines()

prev_rx = int(prev_rx)
prev_tx = int(prev_tx)
prev_time = int(prev_time)

time_diff = cur_time - prev_time
# print(time_diff)
# print(type(time_diff))

# prevent division by zero
# Could catch the exception, but...
if time_diff <= 0:
     exit()

cur_rx = str(cur_rx)
cur_tx = str(cur_tx)
cur_time = str(cur_time)

cur_stats = [cur_rx, cur_tx, cur_time]
# only runs once, need to
# store the value outside the program
# save the current rate to the file.
# Opening a file for writing removes the
# content of that file
# print('cur_rx: ', cur_rx, 'cur_time: ', cur_time)
with open('/tmp/prev_stats_file', 'w') as f:
    f.write('\n'.join(cur_stats))

rx_diff = int(cur_rx) - int(prev_rx)
rx_rate = rx_diff / time_diff
tx_diff = int(cur_tx) - int(prev_tx)
tx_rate = tx_diff / time_diff

# print('rx rate: ', rx_rate)
# print('tx rate: ', tx_rate)

if tx_rate > 1000:
    tx_colour = '#00FF00'
else:
    tx_colour = '#595959'

if rx_rate > 1000:
    rx_colour = '#00FF00'
else:
    rx_colour = '#595959'

# print('<span color=rx_colour></span> <span color=tx_colour></span>')
# <span foreground="red" size="x-large">Roses</span> and <i><span color="#EE37B8">violets</span></i>
print('<span foreground="{}"></span> <span color="{}"></span>'.format(tx_colour, rx_colour))
# print('<span foreground="{}"></span>span foreground="{}"></span>'.format(tx_colour,rx_colour))
