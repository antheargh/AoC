#!/usr/bin/env python3

import sys
from copy import deepcopy

# Run with input file name/path as single argument

def main(inputf):
    n = []
    with open(inputf) as f:
        for line in f:
            n.append(int(line))

    ans_1 = pt_1(deepcopy(n))
    print(ans_1)


def pt_1(n):
    while len(n):
        a = n.pop(0)
        for b in n:
            if a + b == 2020:
                return a*b



if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

