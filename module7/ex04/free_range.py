#!/usr/bin/python3
import sys
if len(sys.argv) < 3:
    print("none")
else:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    arr = []
    for n in range(n1, n2 + 1):
        arr.append(n)
    print(arr)
