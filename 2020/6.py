#!/usr/bin/env python3

import sys
from copy import deepcopy


# Run with input file name/path as single argument

def main(inputf):
    groups = []
    with open(inputf) as f:
        yes = []
        for line in f:
            if line == "\n":
                groups.append(yes)
                yes = []
            else:
                yes.append(line.strip())
        groups.append(yes)


    ans_1 = pt_1(deepcopy(groups))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(groups):
    count = 0
    for g in groups:
        yes_set = set()
        for yes in g:
            yes_set.update([i for i in yes])
        count += len(yes_set)

    return count


def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

