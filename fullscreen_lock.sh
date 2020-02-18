#! /usr/bin/env bash
MSG=${1:-"I'll be right back!"}
PAGE_PORT=${2:-8080}

source ./venv/bin/activate && python3 berightback.py -m "$MSG" &
firefox -new-instance -P "webcam" --kiosk "http://0.0.0.0:$PAGE_PORT" &
sleep .5 && xdotool search --sync --onlyvisible --name "$MSG" windowactivate key F11
xtrlock &
LOCK_PID=$!
wait $LOCK_PID
pkill -P $$
pkill -f berightback
pkill motion
reset
clear
