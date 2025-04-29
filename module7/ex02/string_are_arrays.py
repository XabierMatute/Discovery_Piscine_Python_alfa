#!/usr/bin/python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    for c in sys.argv[1]:
        if c == 'z':
            print(c, end='')
