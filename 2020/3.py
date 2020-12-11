#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np

# Run with input file name/path as single argument

BLANK = '.'
TREE = '#'

def main(inputf):
    map = []
    with open(inputf) as f:
        for line in f:
            map.append([i for i in line.strip()])

    map = np.array(map)
    print(map)
    print(map.shape)


    ans_1 = pt_1(deepcopy(map))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(map):
    (x, y) = (0, 0)
    n_trees = 0
    if map[y, x] == TREE:
        n_trees += 1

    while y < map.shape[0]-1:
        x = (x+3) % (map.shape[1])
        y += 1
        if map[y, x] == TREE:
            n_trees += 1

    return n_trees




def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

