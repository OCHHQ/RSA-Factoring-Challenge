#!/usr/bin/python3
from sys import argv

with open(argv[1]) as f:
    for line in f:
        num = int(line.strip())
        print("{}=".format(num), end='')
        if num % 2 == 0:
            print("{}*2".format(num//2))
            continue
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                print(i, end='')
                num //= i
                if num != 1:
                    print("*", end='')
        if num > 2:
            print("*{}".format(num))
        else:
            print()

