#!/usr/bin/env python3

import subprocess
import re

raw = subprocess.run(['/bin/ip', 'route', 'get', '8.8.4.4'], stdout=subprocess.PIPE)
ip_raw = raw.stdout.decode("utf-8")

m = re.search('src (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ip_raw)
ip = m.group(1)

 
full_text = ip
short_text =  full_text
colour = "#00FF00" # 


print(short_text)
print(full_text)
print(colour)
