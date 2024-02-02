#!/bin/bash

while read line; do
    mline=$(echo "$line" | sed 's/SA://')
    echo "$mline" >> "donnees.csv"
    mac=$(echo "$mline" | cut -d ";" -f4)
    if ! grep -q "$mac" "whitelist.txt"; then
        echo "$mac" >> "whitelist.txt"
        echo "$mac" >> "new.txt"
    fi
done

