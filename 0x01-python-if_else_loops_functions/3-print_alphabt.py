#!/usr/bin/python3
for letters in range(ord('a'), ord('z') + 1):
    if letters == ord('q') or letters == ord('e'):
        continue
    print("{}".format(chr(letters)), end="")
