#!/usr/bin/env python3

import sys
from copy import deepcopy


# Run with input file name/path as single argument

def main(inputf):
    code = []
    with open(inputf) as f:
        for line in f:
            l = line.strip().split(' ')
            code.append([l[0], int(l[1])])

    ans_1 = pt_1(deepcopy(code))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(code):
    acc = 0
    index = 0
    visited = []
    while True:
        visited.append(index)
        (ins, n) = code[index]
        if ins == "nop":
            index += 1
        elif ins == "acc":
            index += 1
            acc += n
        else:
            index += n
        if index in visited:
            break
    return acc




def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

