#!/usr/bin/env python3

import sys
from copy import deepcopy


# Run with input file name/path as single argument

# --- Day 5: Binary Boarding ---
#
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is
# yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport
# control.
#
# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
# perhaps you can find your seat through process of elimination.

def main(inputf):
    seats = []
    with open(inputf) as f:
        for line in f:
            seats.append(line.strip())

    ans_1 = pt_1(deepcopy(seats))
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(seats):
    ids = []
    for seat in seats:
        rows = list(range(128))
        cols = list(range(8))
        pt1, pt2 = seat[:-3], seat[-3:]

        for r in pt1:

            if r == "F":
                rows = rows[:int(len(rows)/2)]
            else:
                rows = rows[int(len(rows)/2):]
        row = rows[0]
        for c in pt2:
            if c == "L":
                cols = cols[:int(len(cols)/2)]
            else:
                cols = cols[int(len(cols)/2):]
        col = cols[0]
        id = row*8 + col
        ids.append(id)

    return max(ids)








def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

