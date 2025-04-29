#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    print("none")
else:
    for s in sys.argv[1:]:
        if s[-3:] != "ism":
            print(s + "ism")
        else:
            print(s)
