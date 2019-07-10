"""
You are given an array and you need to find
number of tripets of indices (i, j, k)  such that the
elements at those indices are in geometric
progression for a given common ratio r and i < j < k.

For example, arr = [1, 4, 16, 64]. If r = 4 , we have
[1, 4, 16] and [4, 16, 64] at indices (0,1,2) and
(1, 2, 3)
https://www.hackerrank.com/challenges/count-triplets-1/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.


def pick_three(n):
    if n < 3:
        return 0
    return math.factorial(n) / 6 / math.factorial(n - 3)


def countTriplets(arr, r):
    index_dict = dict()
    for index, ele in enumerate(arr):
        if ele in index_dict:
            index_dict[ele].append(index)
        else:
            index_dict[ele] = [index]

    triplet_count = 0
    for index, ele in enumerate(arr):
        gp = ele
        while gp in index_dict:
            gp *= r
            if gp in
    print(index_dict)
    return 0


if __name__ == '__main__':
    nr = input().rstrip().split()

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
