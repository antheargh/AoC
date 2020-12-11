#!/usr/bin/env python3

import sys
from copy import deepcopy
import re

# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            entries = re.split(' ', line.strip())
            lim = re.search("(\d+)\-(\d+)", entries[0]).group(1, 2)
            char = entries[1][0]
            data.append([lim, char, entries[2]])

    ans_1 = pt_1(deepcopy(data))
    print(ans_1)

    ans_2 = pt_2(deepcopy(data))
    print(ans_2)


def pt_1(data):
    valid = []
    for d in data:
        min, max = int(d[0][0]), int(d[0][1])
        char = d[1]
        pw = d[2]
        if min <= len(re.findall(char, pw)) <= max:
            valid.append(pw)

    return len(valid)



def pt_2(data):
    valid = []
    for d in data:
        p1, p2 = int(d[0][0]), int(d[0][1])
        char = d[1]
        pw = d[2]
        if (pw[p1-1] == char and pw[p2-1] != char) or (pw[p2-1] == char and pw[p1-1] != char):
            valid.append(pw)

    return len(valid)




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

