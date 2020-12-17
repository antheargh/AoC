#!/usr/bin/env python3

import sys
from copy import deepcopy


# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append(line.strip())

    arrival = int(data[0])
    buses = data[1].split(',')


    ans_1 = pt_1(arrival, buses)
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(arrival, buses):
    bus_n = 0
    buses = list(set(buses) - {"x"})
    buses = list(map(int, buses))
    time = arrival
    while not bus_n:
        time += 1
        for b in buses:
            if time % b == 0:
                bus_n = b
    return (time-arrival)*bus_n



def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

