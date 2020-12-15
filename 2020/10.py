#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np

# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append(int(line))


    ans_1 = pt_1(deepcopy(data))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(data):
    data.sort()
    shifted = [0] + data[:-1]
    data = np.array(data)
    shifted = np.array(shifted)
    joltdiff = (data - shifted).tolist()
    diff1, diff3 = joltdiff.count(1), joltdiff.count(3) + 1 # Add one due to the adaptor having a difference of 3
    print(diff1, diff3)
    return diff1*diff3



def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

