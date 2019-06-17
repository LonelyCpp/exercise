"""
Given an array  of  integers and a number, d, 
perform d left rotations on the array. Return 
the updated array to be printed as a single line 
of space-separated integers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    d = d % len(a)
    if d is 0:
        return a
    new_arr = []
    for i in range(len(a)):
        new_pos = (i - d) % len(a)
        new_arr.insert(new_pos, a[i])
    return new_arr


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
