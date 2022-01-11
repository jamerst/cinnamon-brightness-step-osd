# cinnamon-brightness-step-osd
The brightness steps in Cinnamon are too large for my liking - they don't allow you to select just the right brightness, particularly at low levels.

The minimum brightness also turns the screen off completely, which is annoying.

This script works around that by using a different step amount depending on the percentage, whilst still displaying the native Cinnamon OSD.

It is very similar to my [other script](https://github.com/jamerst/cinnamon-volume-step-osd) for changing the volume step amount.

## Usage
    python brightness-change.py [up|down]

I would recommend compiling the script to a .pyc if binding it to a keyboard shortcut, as with the volume script.