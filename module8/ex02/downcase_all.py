#!/usr/bin/python3
def downcase_it(s : str):
    return s.lower()

import sys
if len(sys.argv) < 2:
    print("none")
else:
    for s in sys.argv[1:]:
        print(downcase_it(s))