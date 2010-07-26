#!/bin/bash

dbus-send --type=method_call --dest=org.kde.klipper /klipper org.kde.klipper.klipper.setClipboardContents string:"`python ~/src/kde_unite/unite.py $1`"
