#!/usr/bin/env python3

import sys
from copy import deepcopy
import re
import itertools


# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append((line.strip()).split(" = "))

    print(data)



    ans_1 = pt_1(deepcopy(data))
    print(ans_1)

    ans_2 = pt_2(deepcopy(data))
    print(ans_2)


def pt_1(data):
    mem = {}
    for d in data:
        if d[0] == "mask":
            mask = {n: b for n, b in enumerate(d[1]) if b != "X"}
        else:
            loc = int(re.search("(\d+)", d[0]).group(0))
            to_write = [b for b in "{:036b}".format(int(d[1]))]
            for n, b in mask.items():
                to_write[n] = b
            mem[loc] = "".join(to_write)

    # Convert back to dec
    sum = 0
    for loc, bin in mem.items():
        if int(bin):
            sum += int(int(bin, 2))

    return sum


def pt_2(data):
    mem = {}
    for d in data:
        if d[0] == "mask":
            mask_1 = [n for n, b in enumerate(d[1]) if b == "1"]
            mask_x = [n for n, b in enumerate(d[1]) if b == "X"]
        else:
            loc = int(re.search("(\d+)", d[0]).group(0))
            loc_bin = [b for b in "{:036b}".format(loc)]
            floats = list(itertools.product([0, 1], repeat=len(mask_x)))
            for i in mask_1:
                loc_bin[i] = "1"
            for f in floats:
                curr_loc = loc_bin
                for i, x in enumerate(mask_x):
                    curr_loc[x] = str(f[i])
                mem[''.join(curr_loc)] = int(d[1])

    return sum(mem.values())



if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

