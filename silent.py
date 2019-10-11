#!/usr/bin/env python3
# Silent collatzer

import sys

cycles = [1, -1, -5, -17]

def collatz(initial):
    n = initial
    while n not in cycles:
        if n % 2: # odd number
            n = (3 * n) + 1
        else:
            n = n >> 1
        if n == initial:
            raise RuntimeError(f'{n} == {initial}')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "neg":
        x = -1
        while True:
            collatz(x)
            x -= 1
    else:
        x = 1
        while True:
            collatz(x)
            x += 1