#!/usr/bin/env python3

import sys
from copy import deepcopy
import re


# Run with input file name/path as single argument

def main(inputf):
    rules = []
    with open(inputf) as f:
        for line in f:
            rules.append(line.strip())

    print(rules)

    ans_1 = pt_1(deepcopy(rules), "shiny gold")
    print(ans_1)

    ans_2 = pt_2()
    print(ans_2)


def pt_1(rules, bag_c):
    # Get list of all colours
    colours = []
    for rule in rules:
        colours.append(re.search("(.+) bags ", rule).group(1))

    # Dict of what bags can contain that coloured bag
    bag_dict = dict()
    for colour in colours:
        print(colour)
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
    return(len(set(parent_bags)))



def pt_2():
    pass




if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

