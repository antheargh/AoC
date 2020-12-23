#!/usr/bin/env python3

import sys
from copy import deepcopy

# Run with input file name/path as single argument

def main(inputf):
    numbers = []
    with open(inputf) as f:
        for line in f:
            numbers.extend(map(int, line.strip().split(',')))

    print(numbers)

    ans_1 = pt_1(deepcopy(numbers))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(numbers):
    turn = len(numbers)
    while turn < 2020:
        last_n = numbers[-1]
        freq = numbers.count(last_n)
        if freq <= 1:
            numbers.append(0)
        else:
            found = False
            for i, n in reversed(list(enumerate(numbers))):
                if n == last_n:
                    if not found:
                        i1 = i
                        found = True
                    elif found:
                        i2 = i
                        break
            numbers.append(i1-i2)
        turn += 1
    return numbers[-1]



def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

