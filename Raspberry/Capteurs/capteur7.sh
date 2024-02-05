#!/bin/bash

while true; do
    data=$(sudo tcpdump -i wlan1mon -e type data -c 1 2>/dev/null)
    mac=$(echo "$data" | cut -d" " -f13 | cut -d ":" -f2-)
    echo "$data" | awk '{print "7;" $1 ";" $7 ";" $16}' | nc -w0 192.168.43.52 12345
done
