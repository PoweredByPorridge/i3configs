#!/usr/bin/env python3

import re
import subprocess

# The second parameter overrides the mixer selection
# For PulseAudio users, use "pulse"
# For Jack/Jack2 users, use "jackplug"
# For ALSA users, you may use "default" for your primary card
# or you may use hw:# where # is the number of the card desired


mix_raw = subprocess.run(['lsmod'], stdout=subprocess.PIPE)
mix = mix_raw.stdout.decode("utf-8")

if "pulse " in mix:
    mixer = "pulse"
elif "jack " in mix:
    mixer = "jack"
else:
    mixer ="default"

# The instance option sets the control to report and configure
# This defaults to the first control of your selected mixer
# For a list of the available, use `amixer -D $Your_Mixer scontrols`

ctrl_raw = subprocess.run(['amixer', '-D', mixer, 'scontrols'], stdout=subprocess.PIPE)
ctrl = ctrl_raw.stdout.decode("utf-8")

m = re.search("'(\w+)'", ctrl)
control = m.group(1)

# print(control)

get_vol_raw = subprocess.run(['amixer', 'get', control], stdout=subprocess.PIPE)
get_vol = get_vol_raw.stdout.decode("utf-8")

vol = re.search("\[(\d+)\%]", get_vol)

volume = int(vol.group(1))

colour="#009900" # Green.

if volume > 99:
    VOLUME_ICON=""
    colour="#FF0000" # Red.
elif volume > 90:
    VOLUME_ICON="9"
elif volume > 80:
     VOLUME_ICON="8"
elif volume > 70:
     VOLUME_ICON="7"
elif volume > 60:
     VOLUME_ICON="6"
elif volume > 50:
     VOLUME_ICON="5"
elif volume > 40:
     VOLUME_ICON="4"
elif volume > 30:
     VOLUME_ICON="3"
elif volume > 20:
     VOLUME_ICON="2"
elif volume > 10:
     VOLUME_ICON="1"
else:
     VOLUME_ICON="-"


full_text=VOLUME_ICON
short_text=full_text
print(short_text)
print(full_text)
print(colour)

