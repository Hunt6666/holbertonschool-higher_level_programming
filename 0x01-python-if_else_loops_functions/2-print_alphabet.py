#!/usr/bin/python3
# prints alphabet
# print("abcdefghijklmnopqrstuvwxyz", end = '\0')
for i in range(0, 26):
    print("{:s}" .format(chr(i + 97)), end='')
