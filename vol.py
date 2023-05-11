#!/usr/bin/env python3

import subprocess

raw = subprocess.run(['/usr/share/i3blocks/volume'], stdout=subprocess.PIPE)
vol_raw = raw.stdout.decode("utf-8")

# Need to reMove the last two charaCters as raw.stdout.decode("utf-8")
# returns a string with a newline: "39%\n"
vol = vol_raw[:-2]

volume = int(vol)
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

# echo "${VOLUME_ICON}"

# This was the 20 echo $VOLUME

# ifvolume > 90:
#      VOLUME_ICON="█"
# elif volume > 80:
#      VOLUME_ICON="▇"
# elif volume > 70:
#      VOLUME_ICON="▆"
# elif volume > 60:
#      VOLUME_ICON="▅"
# elif volume > 50:
#      VOLUME_ICON="▄"
# elif volume > 40:
#      VOLUME_ICON="▃"
# elif volume > 30:
#      VOLUME_ICON="▂"
# elif volume > 20:
#      VOLUME_ICON="▁"
# elif [[ "${VOLUME}" -le 10:
#      VOLUME_ICON="-"
# fi

