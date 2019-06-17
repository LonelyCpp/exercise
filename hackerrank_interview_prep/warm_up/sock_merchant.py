"""
John works at a clothing store. He has a large pile of socks 
that he must pair by color for sale. Given an array of integers 
representing the color of each sock, determine how many pairs 
of socks with matching colors there are.

For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. 
There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. 
The number of pairs is 2.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    count = dict()
    for soc in ar:
        if soc in count:
            count[soc] += 1
        else:
            count[soc] = 1

    pair_count = 0
    for color in count:
        pair_count += count[color] // 2
    return pair_count


if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
