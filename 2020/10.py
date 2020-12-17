#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np
import itertools

# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append(int(line))


    ans_1 = pt_1(deepcopy(data))
    print(ans_1)

    ans_2 = pt_2(deepcopy(data))
    print(ans_2)


def pt_1(data):
    data.sort()
    shifted = [0] + data[:-1]
    data = np.array(data)
    shifted = np.array(shifted)
    joltdiff = (data - shifted).tolist()
    diff1, diff3 = joltdiff.count(1), joltdiff.count(3) + 1 # Add one due to the adaptor having a difference of 3
    return diff1*diff3



def pt_2(data):
    data.sort()
    data.append(data[-1]+3)

    shifted = np.array([0]+data[:-1])
    data = np.array(data)

    joltdiff = (data - shifted).tolist()

    n = 1
    consec = 0

    for i in joltdiff:
        if consec and i == 3:
            if consec > 1:
                combinations = calc_comb(consec)
                n *= combinations
            consec = 0
        elif i == 1:
            consec += 1

    return n

def calc_comb(n):
    comb_n = 0
    # Stretch of n consecutive numbers

    # Find amount of combinations of 1, 2, 3 that add up to n
    c_set = set()
    n_1, n_2, n_3 = n, 0, 0
    c_set.add((n_1, n_2, n_3))
    while n_1 > 0:
        n_1 -= 1
        n_2 = 0
        while n_1*1 + n_2*2 + n_3*3 <= n:
            while n_1*1 + n_2*2 + n_3*3 <= n:
                if n_1*1 + n_2*2 + n_3*3 == n:
                    c_set.add((n_1, n_2, n_3))
                n_3 += 1
            n_2 += 1
            n_3 = 0
    c_list = list(c_set)

    # Find unique permutations of those combinations

    for c in c_list:
        totals = [1]*c[0] + [2]*c[1] + [3]*c[2]
        perms = set(itertools.permutations(totals)) # Get rid of duplicates
        comb_n += len(perms)

    return comb_n






if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

