#!/usr/bin/env python3

import re
import time
import subprocess

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
    cur_rx = int(f.read())
    # print("current_rx: ", cur_rx, type(cur_rx))

f = open('/tmp/prev_file', 'r')
f.seek(0)
prev_rx, prev_time = f.readlines()
f.close()

prev_rx = int(prev_rx)
prev_time = int(prev_time)

# print("prev_rx", prev_rx, type(prev_rx))
# print("prev_time", prev_time, type(prev_time))

time_diff = (cur_time - prev_time) + 10
# print(time_diff)
# print(type(time_diff))

# prevent division by zero
# Could catch the exception, but...
if time_diff <= 0:
     exit()

# only runs once, need to
# store the value outside the program
# save the current rate to the file.
# Opening a file for writing removes the
# content of that file
cur_rx = str(cur_rx)
cur_time = str(cur_time)
prev_rx_time = [cur_rx, cur_time]
# print("cur_rx: ", cur_rx, "cur_time: ", cur_time)

f = open('/tmp/prev_file', 'w')
f.write("\n".join(prev_rx_time))
f.close()

rx_diff = int(cur_rx) - int(prev_rx)
# print(time_diff)
rx_rate = rx_diff / (time_diff + 1)

if rx_rate > 1000:
    full_text=""
    short_text=full_text
    colour="#00FF00"
else:
    full_text=""
    short_text=full_text
    colour="#595959" # a grotty grey

print(full_text)
print(short_text)
print(colour)
