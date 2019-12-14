MSG=${1:-"I'll be right back!"}
PAGE_PORT=${2:-8080}

cd ~/dev/webcam_shower/ && source venv/bin/activate
python berightback.py -m "$MSG" &
firefox -new-instance -P "webcam" --kiosk "http://0.0.0.0:$PAGE_PORT" &
sleep .5 && xdotool search --sync --onlyvisible --name "$MSG" windowactivate key F11
xtrlock &
LOCK_PID=$!
wait $LOCK_PID
pkill -P $$
# kill -9 $WC_PID
reset
clear
