#! /bin/sh

# Start Vnc Server
/opt/entrypoint.sh > vnc.log 2>&1 & 

# Wait for Vnc Server to start
until pids=$(pidof x11vnc)
do   
    sleep 1
done

sleep 5

# Start Python script
python3 ./src/main.py