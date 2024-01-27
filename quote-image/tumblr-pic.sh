#!/bin/bash

# Der vollständige Pfad zum 'screen'-Befehl
SCREEN="/usr/bin/screen"

# Der vollständige Pfad zum 'python3'-Befehl
PYTHON="/usr/bin/python3"

# Starte die zweite Screen-Session für daily.py im Hintergrund
$SCREEN -dmS tumblr-bild-session

# Wechsle in der Screen-Session in das Verzeichnis und führe daily.py aus
$SCREEN -S tumblr-bild-session -X stuff "cd /var/script/data/tumblr_bild && sleep 60 && $PYTHON main.py\n"
