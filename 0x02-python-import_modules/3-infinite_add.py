#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]

    integers = (int(arg) for arg in argv)
    total = sum(integers)
    print(total)
