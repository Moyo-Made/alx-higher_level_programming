#!/usr/bin/python3
for ascii_char in range(ord('z'), ord('a') -1, -1):
    print(chr(ascii_char).lower() if (ord('z') - ascii_char) % 2 == 0 else chr(ascii_char).upper(), end="")
print(end="")
