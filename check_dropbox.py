#!/usr/bin/env python3

import subprocess
dropbox_status = subprocess.run(['dropbox', 'status'], stdout=subprocess.PIPE)
db_status = dropbox_status.stdout.decode('utf-8')

# print(db_status)

if db_status == "Up to date\n":
    full_text = "DBOX"
    short_text = full_text
    colour="#00FF00" # Green. It's up to date.
elif db_status == "Dropbox isn't running!\n":
    full_text="DBOX"
    short_text = full_text
    colour="#FF0000" # Red. It's not running.
else:
    full_text="DBOX"
    short_text = full_text
    colour="#FFA500" # Anything else is orange.


print(short_text)
print(full_text)
print(colour)
