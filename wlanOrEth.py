#!/usr/bin/env python3

import socket
import re
import subprocess

raw = subprocess.run(['/bin/ip', 'route'], stdout=subprocess.PIPE)
ip_raw = raw.stdout.decode("utf-8")

hostname = socket.gethostname()

m = re.search('^(?:\S+ ){4}(\S+)', ip_raw)

interface = m.group(1)

if interface[0:1] == "w":
    print(hostname, "") # full text
    print(hostname, "") # short text
    print("#00FF00") # colour
elif interface[0:1] == "e":
    print(hostname, "") # full text
    print(hostname, "") # short text
    print("#00FF00") # colour

