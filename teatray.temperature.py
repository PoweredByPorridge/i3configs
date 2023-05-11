#!/usr/bin/env python3

import subprocess
import re


# default values
critical_temp = 80
warning_temp = 60
# cpu = "k10temp-pci-00c3" # teapot
cpu = "coretemp-isa-0000" # teatray
temperature = 444;

sensor_read = subprocess.run(['sensors', '-u', cpu], stdout=subprocess.PIPE)
cpu_temp = sensor_read.stdout.decode('utf-8')
# print(cpu_temp)

m = re.search('  temp1_input: (\d+\.\d)', cpu_temp)
temp_out = float(m.group(1))

if temp_out >= critical_temp:
    full_text = temp_out
    short_text = full_text
    colour="#FF0000" # Red. We're burning up.
elif temp_out >= warning_temp:
    full_text = temp_out
    short_text = full_text
    colour="#FFA500" # Orange. You could fry on that.
else:
    full_text = temp_out
    short_text = full_text
    colour="#00FF00" # Green. All is sweetness and light.


print(f"{short_text}°C")
print(f"{full_text}°C")
print(colour)
