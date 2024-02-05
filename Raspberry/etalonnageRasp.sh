#!/bin/bash

mac=""
nb=2

data=$(sudo tcpdump -i wlan1mon -c "$nb" -e type mgt subtype probe-req and ether host "$mac" 2>/dev/null)
echo "$data" | awk '{print "1;" $1 ";" $7 ";" $13}' | nc -w0 192.168.43.52 12345