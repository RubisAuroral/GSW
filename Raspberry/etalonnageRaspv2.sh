#!/bin/bash

mac="00:b5:d0:ed:54:3b"
nb=5
capteur=1

data=$(sudo tcpdump -i wlan1mon -c "$nb" -e type data and ether host "$mac" 2>/dev/null)

moyenne=$(echo "$data" | awk -v capteur="$capteur" '
{
    value = $7;
    sub("dBm", "", value);  # Supprimer "dBm" de la valeur
    sum += value;           # Ajouter la valeur à la somme
    count++;                # Compter le nombre de valeurs
}
END {
	printf("%d;%.2f\n", capteur, sum / count);  # Afficher le numéro du capteur et la moyenne
}')

echo "$moyenne" | nc -w0 192.168.43.52 12345
