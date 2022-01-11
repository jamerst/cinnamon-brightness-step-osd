#!/usr/bin/python3

import dbus
import sys

sessionBus = dbus.SessionBus()

brightnessProxy = sessionBus.get_object('org.cinnamon.SettingsDaemon.Power.Screen', '/org/cinnamon/SettingsDaemon/Power')
brightnessInterface = dbus.Interface(brightnessProxy, 'org.cinnamon.SettingsDaemon.Power.Screen')

current = brightnessInterface.GetPercentage()

direction = 1 if sys.argv[1] == "up" else -1

if current <= 1 and direction < 0:
    exit()
elif current == 100 and direction > 0:
    exit()

step = 0
if current < 10 or (current == 10 and direction < 0):
    step = 1
elif current < 20 or (current == 20 and direction < 0):
    step = 2
else:
    step = 5

new = current + direction * step

if new > 100:
    new = 100
elif new < 1:
    new = 1

brightnessInterface.SetPercentage(new)

osdProxy = sessionBus.get_object('org.Cinnamon', '/org/Cinnamon')
osdInterface = dbus.Interface(osdProxy, 'org.Cinnamon')
osdInterface.ShowOSD({ "icon": 'display-brightness-symbolic', "level": new })