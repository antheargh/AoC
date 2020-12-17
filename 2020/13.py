#!/usr/bin/env python3

import sys
from copy import deepcopy
import numpy as np

MIN_TIME = 100000000000000

# Run with input file name/path as single argument

def main(inputf):
    data = []
    with open(inputf) as f:
        for line in f:
            data.append(line.strip())

    arrival = int(data[0])
    buses = data[1].split(',')


    ans_1 = pt_1(arrival, deepcopy(buses))
    print(ans_1)

    ans_2 = pt_2(deepcopy(buses))
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



def pt_2(buses):
    bus_dict = {}
    for n, b in enumerate(buses):
        if b == "x":
            pass
        else:
            bus_dict[int(b)] = (int(b) - n) % int(b)
    print(bus_dict)
    time = 0
    increment = 1
    for b, n in bus_dict.items():
        while time % b != n:
            time += increment
        increment *= b

    return time





if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)


