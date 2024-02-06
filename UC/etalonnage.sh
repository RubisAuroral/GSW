#!/bin/bash

capteurs=1

for (( i=0; i<capteurs; i++ )); do
	nc -l 12345
done