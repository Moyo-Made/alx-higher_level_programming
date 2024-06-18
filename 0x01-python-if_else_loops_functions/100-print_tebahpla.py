#!/usr/bin/python3
for ascii_char in range(ord('z'), ord('a') - 1, -1):
    character = chr(ascii_char).lower() if (ord('z') - ascii_char) % 2 == 0 \
            else chr(ascii_char).upper()
    print("{}".format(character), end="")
print(end="")
