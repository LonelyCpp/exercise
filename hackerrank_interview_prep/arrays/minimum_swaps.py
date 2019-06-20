#!/bin/python3
"""
You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap
any two elements. You need to find the minimum number of swaps
required to sort the array in ascending order.
"""


def minimum_swaps(arr):
    swaps = 0
    for index, val in enumerate(arr):
        if arr[index] == index + 1:
            continue
        while arr[index] != index + 1:
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
            swaps += 1

    return swaps


if __name__ == '__main__':
    print(minimum_swaps([2, 3, 4, 1, 5]))
