#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    print("none")
else:
    for s in reversed(sys.argv[1:]):
        print(s)