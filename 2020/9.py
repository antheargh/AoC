#!/usr/bin/env python3

import sys
from copy import deepcopy


# Run with input file name/path as single argument

def main(inputf):
    nums = []
    with open(inputf) as f:
        for line in f:
            nums.append(int(line))

    ans_1 = pt_1(deepcopy(nums))
    print(ans_1)

    ans_2 = pt_2(deepcopy(nums), ans_1)
    print(ans_2)


def pt_1(nums):
    preamble = nums[:25]
    for n in nums[25:]:
        if not in_preamble(deepcopy(preamble), n):
            target = n
            break
        else:
            preamble.pop(0)
            preamble.append(n)
    return target

def in_preamble(preamble, n):
    while len(preamble):
        a = preamble.pop(0)
        for b in preamble:
            if a + b == n:
                return True
    return False


def pt_2(nums, target):
    for i, n in enumerate(nums):
        sum = n
        j = i + 1
        while sum < target:
            sum += nums[j]
            if sum == target:
                sum_list = nums[i:j+1]
                return min(sum_list) + max(sum_list)
            j += 1



if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

