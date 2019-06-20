#!/bin/python3
"""
You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap
any two elements. You need to find the minimum number of swaps
required to sort the array in ascending order.
"""


def minimum_swaps(arr):
    swaps = 0
    first = 0
    last = len(arr) - 1
    swaps = 0
    while first < last:
        while (arr[first] == first + 1 and first < last):
            first += 1
        if first < last:
            temp = arr[arr[first] - 1]
            arr[arr[first] - 1] = arr[first]
            arr[first] = temp
            swaps += 1

    return swaps


if __name__ == '__main__':
    print(minimum_swaps([1, 3, 5, 4]))
