#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np

EMPTY = "L"
OCC = "#"
FLOOR = "."

# Run with input file name/path as single argument

def main(inputf):
    map = []
    with open(inputf) as f:
        for line in f:
            map.append([i for i in line.strip()])



    ans_1 = pt_1(deepcopy(map))
    print(ans_1)

    ans_2 = pt_2(deepcopy(map))
    print(ans_2)

class Seats():
    def __init__(self, map, mode):
        self.basemap = np.array(map)
        self.map = np.array(map)
        self.count = 0
        self.rows, self.cols = self.map.shape
        self.mode = mode

    def round(self, p=0):
        self.count += 1
        n_changes = 0
        nextmap = deepcopy(self.map) # Map on the next round
        if self.mode == 1:
            min_n = 4
        else:
            min_n = 5


        # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        # Otherwise, the seat's state does not change.
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mode == 1:
                    adj = self.get_adj(r, c)
                else:
                    adj = self.get_visible_adj(r, c)
                if self.map[r, c] == EMPTY:
                    for (i, j) in adj:
                        if self.map[i, j] == OCC:
                            break
                    else:
                        nextmap[r, c] = OCC
                        n_changes += 1
                if self.map[r, c] == OCC:
                    occ_n = 0
                    for (i, j) in adj:
                        if self.map[i, j] == OCC:
                            occ_n += 1
                    if occ_n >= min_n:
                        nextmap[r, c] = EMPTY
                        n_changes += 1



        self.map = nextmap
        if p:
            print(self.map)

        return n_changes

    def get_adj(self, r, c):
        adj_list = []
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i >= 0 and i < self.rows and j >= 0 and j < self.cols:
                    if (i, j) != (r, c):
                        adj_list.append((i, j))
        return adj_list

    def get_visible_adj(self, r, c):
        adj_list = []

        shifts = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for shift in shifts:
            i, j = r, c
            in_bounds = True
            while in_bounds:
                i += shift[0]
                j += shift[1]
                if not (0 <= i < self.rows and 0 <= j < self.cols):
                    break
                if self.basemap[i, j] == EMPTY:
                    adj_list.append((i, j))
                    break

        return adj_list




    def count_occ(self):
        return (self.map == OCC).sum()


def pt_1(map):
    seats = Seats(map, mode=1)
    changed = 1
    while changed:
        changed = seats.round()
    return seats.count_occ()



def pt_2(map):
    seats = Seats(map, mode=2)
    changed = 1
    while changed:
        changed = seats.round()
    return seats.count_occ()




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

