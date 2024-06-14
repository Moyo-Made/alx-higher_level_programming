#!/usr/bin/python3
excluded_letters = {"q", "e"}
for ascii_value in range(97, 123):
    letter = chr(ascii_value)
    if letter not in excluded_letters:
        print("{}".format(letter), end="")
