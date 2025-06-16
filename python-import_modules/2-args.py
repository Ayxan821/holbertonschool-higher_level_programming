#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # argv[0] proqramın adı, onu atırıq
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    for i in range(count):
        print(f"{i + 1}: {argv[i]}")
