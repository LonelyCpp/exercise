"""
Starting with a 1-indexed array of zeros and 
a list of operations, for each operation add 
a value to each of the array element between 
two given indices, inclusive. Once all operations 
have been performed, return the maximum value 
in your array.
https://www.hackerrank.com/challenges/crush/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    diff_dict = dict()
    for query in queries:
        if query[0] in diff_dict.keys():
            diff_dict[query[0]] += query[2]
        else:
            diff_dict[query[0]] = query[2]

        if query[1] + 1 in diff_dict.keys():
            diff_dict[query[1] + 1] -= query[2]
        else:
            diff_dict[query[1] + 1] = -query[2]

    sortedIndices = list(diff_dict)
    sortedIndices.sort()
    max_num = current_sum = 0

    print(diff_dict)
    for sortedIndex in sortedIndices:
        current_sum += diff_dict[sortedIndex]
        max_num = max(max_num, current_sum)
    return max_num


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
