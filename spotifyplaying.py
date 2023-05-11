#!/usr/bin/env python3


import subprocess

artist_raw = subprocess.run(['playerctl', 'metadata', 'artist'], stdout=subprocess.PIPE)
artist = artist_raw.stdout.decode("utf-8")
# The decoded string ends with a "\n" so it needs to be removed.
artist = artist.rstrip("\n")

title_raw = subprocess.run(['playerctl', 'metadata', 'title'], stdout=subprocess.PIPE)
title = title_raw.stdout.decode("utf-8")
title = title.rstrip("\n")

if artist:
    print(" " + artist + " --- " + title)
else:
    pass
