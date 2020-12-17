#!/usr/bin/env python3

import sys
from copy import deepcopy
import re


# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append((line.strip()).split(" = "))

    print(data)



    ans_1 = pt_1(deepcopy(data))
    print(ans_1)

    ans_2 = pt_2()
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


def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

