#!/bin/bash

while read line; do
    mline=$(echo "$line" | sed 's/SA://' | sed -E 's/(-?[0-9]+)dBm/\1/')

    echo "$mline" >> "donnees.csv"

    mac=$(echo "$mline" | cut -d ";" -f4)

    if ! grep -q "$mac" "whitelist.txt"; then
        echo "$mac" >> "whitelist.txt"
        echo "$mac" >> "new.txt"
    fi
done
