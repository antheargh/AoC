#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np

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

    ans_2 = pt_2(deepcopy(instructions))
    print(ans_2)

class Ship:
    def __init__(self):
        self.ew = 0
        self.ns = 0
        self.facing = 0
        self.wp_ew = 10
        self.wp_ns = 1

    def move1(self, dir, n):
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

    def move2(self, dir, n):
        if dir in NEWS:
            self.wp_ew += NEWS_DICT[dir][0] * n
            self.wp_ns += NEWS_DICT[dir][1] * n
        elif dir in LR:
            print("Initially:", self.wp_ew, self.wp_ns)
            shift = int(n/90)
            for _ in range(shift):
                ew, ns = self.wp_ew, self.wp_ns
                if dir == "R":
                    self.wp_ns = -1 * ew
                    self.wp_ew = ns
                else:
                    self.wp_ns = ew
                    self.wp_ew = -1 * ns
        elif dir == FORWARD:
            self.ew += self.wp_ew * n
            self.ns += self.wp_ns * n





def pt_1(ins):
    ship1 = Ship()
    for i in ins:
        ship1.move1(*i)
    return abs(ship1.ns) + abs(ship1.ew)




def pt_2(ins):
    ship2 = Ship()
    for i in ins:
        ship2.move2(*i)
        print(ship2.wp_ew, ship2.wp_ns)
    return abs(ship2.ns) + abs(ship2.ew)




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

