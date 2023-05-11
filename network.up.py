#!/usr/bin/env python3

import re
import time
import subprocess

# open temp file for appending, jsut to make sure it is there
# then close it again
f = open('/tmp/prev_tx_file', 'a')
f.close()

# time is UNIX time, a number. Easier on the system, and
# as I'm not actually interested in it, we'll stick with
# it
cur_time = int(time.time())
# print("cur_time", cur_time, type(cur_time))


raw = subprocess.run(['/bin/ip', 'route'], stdout=subprocess.PIPE)
ip_raw = raw.stdout.decode("utf-8")

m = re.search('^(?:\S+ ){4}(\S+)', ip_raw)
instance = m.group(1)

open_string = "/sys/class/net/" + instance + "/statistics/rx_bytes"
# print(open_string)

# read rx bytes
# No longer assumes that the interface is eth0
with open(open_string) as f:
    cur_tx = int(f.read())

# opens a file fo reading - assumes it exists
# could open as a+ earlier and add two numbers
# to create it
# Rewind, read in the values from the previous run
# and then close the file
f = open('/tmp/prev_tx_file', 'r')
f.seek(0) 
prev_tx, prev_time = f.readlines()
f.close()

prev_tx = int(prev_tx)
prev_time = int(prev_time)

time_diff = cur_time - prev_time
# print(time_diff)
# print(type(time_diff))

# prevent division by zero
# Could catch the exception, but...
# Was time_diff < 0 but that made the output disappear
if time_diff <= 0:
     exit()

# only runs once, need to
# store the value outside the program
# save the current rate to the file.
# Opening a file for writing removes the
# content of that file
cur_tx = str(cur_tx)
cur_time = str(cur_time)
prev_tx_time = [cur_tx, cur_time]


f = open('/tmp/prev_tx_file', 'w')
f.write("\n".join(prev_tx_time))
f.close()

tx_diff = int(cur_tx) - int(prev_tx)
# print(time_diff)
tx_rate = tx_diff / time_diff

if tx_rate > 1000:
    full_text=""
    short_text=full_text
    colour="#00FF00"
else:
    full_text=""
    short_text=full_text
    colour="#595959" # a grotty grey

print(full_text)
print(short_text)
print(colour)
