#!/usr/bin/env python3

import sys
from copy import deepcopy
import re
import numpy as np


# Run with input file name/path as single argument

def main(inputf):
    rules = []
    with open(inputf) as f:
        for line in f:
            rules.append(line.strip())


    ans_1 = pt_1(deepcopy(rules), "shiny gold")
    print(ans_1)

    ans_2 = pt_2(deepcopy(rules), "shiny gold")
    print(ans_2)


def pt_1(rules, bag_c):
    # Get list of all colours
    colours = []
    for rule in rules:
        colours.append(re.search("(.+) bags ", rule).group(1))

    # Dict of bags that the coloured bag is contained by
    bag_dict = dict()
    for colour in colours:
        can_contain = []
        for rule in rules:
            if re.search("\d "+colour, rule):
                can_contain.append(re.search("(.+) bags ", rule).group(1))
        bag_dict[colour] = can_contain

    # Go through find all bags that can contain a root bag
    parent_bags = []
    unchecked = bag_dict[bag_c]
    while len(unchecked):
        next_bag = unchecked.pop()
        parent_bags.append(next_bag)
        if len(bag_dict[next_bag]):
            unchecked.extend(bag_dict[next_bag])
    return len(set(parent_bags))



def pt_2(rules, bag_c):
    bag_dict = dict()

    # Dict of what each coloured bag can contain
    for rule in rules:
        bag = re.search("(.+) bags contain", rule).group(1)
        contains = []
        contained_bags = re.findall("(\d+) (\D+ \D+) bag", rule)
        for b in contained_bags:
            n, c = int(b[0]), b[1]
            contains.append((n, c))
        bag_dict[bag] = contains

    # Use recursion to find total number of bags

    n = calc_total(bag_c, bag_dict)

    return n

def calc_total(bag, bag_dict):
    total = 0
    if bag_dict[bag]:
        for (n, b) in bag_dict[bag]:
            total += n + n*calc_total(b, bag_dict)
    return total



if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

