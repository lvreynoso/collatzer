#!/usr/bin/env python3

import sys

cycles = [1, -1, -5, -17]

def collatz(initial):
    n = initial
    steps = [initial]
    while n not in cycles:
        if n % 2: # odd number
            n = (3 * n) + 1
        else:
            n = n // 2
        if n == initial:
            raise RuntimeError(f'{n} == {initial}')
        steps.append(n)
    print(f'n = {initial}: {len(steps)} steps')
    print(f'sequence: {" -> ".join(map(str, steps))}')
    print('---')

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