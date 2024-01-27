#!/bin/bash

# The complete path to the 'screen' command
SCREEN="/usr/bin/screen"

# The complete path to the 'python3' command
PYTHON="/usr/bin/python3"

# Start the second screen session for daily.py in the background
$SCREEN -dmS tumblr-pic-session

# Change to the directory in the screen session and execute main.py
# I wait 60 seconds here to relieve the system at startup.
$SCREEN -S tumblr-pic-session -X stuff "cd /path/to/your/script && sleep 60 && $PYTHON main.py\n"
