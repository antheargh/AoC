#!/usr/bin/env python3

import sys
from copy import deepcopy

NEWS = ("E", "S", "W", "N")
NEWS_DICT = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}
LR = ("L", "R")
FORWARD = "F"

# Run with input file name/path as single argument

def main(inputf):
    instructions = []
    with open(inputf) as f:
        for line in f:
            instructions.append([line[0], int(line.strip()[1:])])


    ans_1 = pt_1(deepcopy(instructions))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)

class Ship:
    def __init__(self):
        self.ew = 0
        self.ns = 0
        self.facing = 0

    def move(self, dir, n):
        if dir in NEWS:
            self.ew += NEWS_DICT[dir][0]*n
            self.ns += NEWS_DICT[dir][1]*n
        elif dir in LR:
            shift = n/90
            if dir == "L":
                shift *= -1
            self.facing = int((self.facing + shift) % 4)
        elif dir == FORWARD:
            self.ew += NEWS_DICT[NEWS[self.facing]][0] * n
            self.ns += NEWS_DICT[NEWS[self.facing]][1] * n



def pt_1(ins):
    ship = Ship()
    for i in ins:
        ship.move(*i)
    return abs(ship.ns) + abs(ship.ew)




def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

