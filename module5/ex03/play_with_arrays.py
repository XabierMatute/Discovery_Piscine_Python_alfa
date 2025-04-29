#!/usr/bin/python3
array_og = [2, 8, 9, 48, 8, 22, -12, 2]
array_mod = set()
for num in array_og:
    if num >= 5:
        array_mod.add(num + 2)
print(array_og)
print(array_mod)