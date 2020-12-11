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

    ans_1 = pt_1(deepcopy(map))
    print(ans_1)

    ans_2 = pt_2(deepcopy(map))
    print(ans_2)


def pt_1(map):
    n_trees = tree_hits(3, 1, map)

    return n_trees


def pt_2(map):
    dir = ((1,1), (3, 1), (5, 1), (7, 1), (1, 2))
    n_tree_prod = 1
    for (r, d) in dir:
        n_tree_prod *= tree_hits(r, d, map)

    return n_tree_prod


def tree_hits(right, down, map):
    (x, y) = (0, 0)
    n_trees = 0
    if map[y, x] == TREE:
        n_trees += 1

    while y < map.shape[0] - 1:
        x = (x + right) % (map.shape[1])
        y += down
        if map[y, x] == TREE:
            n_trees += 1

    return n_trees




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

