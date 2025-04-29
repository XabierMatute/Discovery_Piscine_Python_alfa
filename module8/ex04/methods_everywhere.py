#!/usr/bin/python3
def shrink(s :str):
    print(s[0:8])

def enlarge(s :str):
    print(s + "ZZZZZZZ"[len(s) - 1:])

import sys
if len(sys.argv) < 2:
    print("none")
else:
    for s in sys.argv[1:]:
        if len(s) > 8:
            shrink(s)
        if len(s) < 8:
            enlarge(s)
        if len(s) == 8:
            print(s)