#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    print("none")
else:
    print("paraparapara: ", len(sys.argv) - 1)
    for s in sys.argv[1:]:
        print(s + ":", len(s))
