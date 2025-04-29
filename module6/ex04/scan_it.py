#!/usr/bin/python3
import sys
import re
if len(sys.argv) < 3:
    print("none")
else:
    clave = sys.argv[1]
    s = sys.argv[2]
    n = len(re.findall(clave, s))
    if n == 0:
        print("none")
    else:
        print(n)