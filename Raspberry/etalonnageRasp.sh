mac="50:da:d6:47:75:aa"
nb=2

while true; do
    data=$(sudo tcpdump -i wlan1mon -e subtype probe-req -c "$nb" ether host "$mac" 2>/dev/null)
    echo "$data" | awk '{print "1;" $1 ";" $7 ";" $13}' | nc -w0 192.168.43.52 12345
done