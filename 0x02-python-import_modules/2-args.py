#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} argument{"s" if argc > 1 else ""}:")
        for i in range(argc):
            print(f"{i + 1}: {argv[i]}")
