# SecHints
Cybersecurity / pentesting tips, hints and tools


## Host Discovery and Enumeration
### LOTL Host Discovery and ARP soliciation
This will not only show ping responses, but will also populate the arp cache, which can show hosts that are dropping ICMP packets. If they want to be reachable by IP, they have to respond to ARP requests.

```bash
for i in $(seq 1 254); do (ping -c 1 10.1.1.${i} | grep "bytes from" &) ;done; sleep 5; ip n | grep REACHABLE  | sort |uniq
```




## SSH Tricks and Hints
### SSH escape sequences
```
> ~?
Supported escape sequences:
 ~.   - terminate connection (and any multiplexed sessions)
 ~B   - send a BREAK to the remote system
 ~C   - open a command line
 ~R   - request rekey
 ~V/v - decrease/increase verbosity (LogLevel)
 ~^Z  - suspend ssh
 ~#   - list forwarded connections
 ~&   - background ssh (when waiting for connections to terminate)
 ~?   - this message
 ~~   - send the escape character by typing it twice
(Note that escapes are only recognized immediately after newline.)
```
