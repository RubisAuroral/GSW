#!/bin/bash

mac="c0:ee:fb:dd:67:9d"
nb=5

data=$(sudo tcpdump -i wlan1mon -c "$nb" -e type data and ether host "$mac" 2>/dev/null)
echo "$data" | awk '{print "1;" $1 ";" $7 ";" $13}' | nc -w0 192.168.43.52 12345