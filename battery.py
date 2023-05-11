#!/usr/bin/env python3

import re
import subprocess

colour = "#FFFFFF"

# acpi queries the battery
raw = subprocess.run(['acpi'], stdout=subprocess.PIPE)
bat_raw = raw.stdout.decode("utf-8")

# regex has to cater for the 100% case where there is no thord group. Though the
# fourth group is actually a subset of the third.
m = re.search('Battery [0-9]: (\w*), (\d{1,3})%(?:(, (\d{2}:\d{2})))?', bat_raw)

# acpi output:
# Battery 0: Charging, 92%, 00:09:42 until charged

# Charging or Discharging
charge_or_discharge = m.group(1)

# Percent full
percent_charge = int(m.group(2))

# minutes until charded or disdharged
mins_until = m.group(4)

if charge_or_discharge == "Full":
    full_text = f"{percent_charge}%"
elif charge_or_discharge == "Charging":
    full_text = f"{percent_charge}% CHR ({mins_until})"
    colour = "#FFFFFF"
elif charge_or_discharge == "Discharging":
    if percent_charge < 20:
        colour = "#FF0000"
    elif percent_charge < 40:
        colour = "#FFAE00"
    elif percent_charge < 60:
        colour = "#FFF600"
    elif percent_charge < 85:
        colour = "#A8FF00"
    elif percent_charge == 100:
        full_text = f"{percent_charge}% "        
    else:
        colour = "#FFFFFF"
    full_text = f"{percent_charge}% DIS ({mins_until})"

print(full_text)
print(full_text)    
print(colour)
