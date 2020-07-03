# SecHints
Cybersecurity / pentesting tips, hints and tools


# LOTL Host Discovery and ARP soliciation
This will not only show ping responses, but will also populate the arp cache, which can show hosts that are dropping ICMP packets. If they want to be reachable by IP, they have to respond to ARP requests.
for i in $(seq 1 254); do (ping -c 1 10.1.1.${i} | grep "bytes from" &) ;done; sleep 5; ip n | grep REACHABLE  | sort |uniq
