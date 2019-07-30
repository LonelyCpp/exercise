"""
If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below n.
"""
import sys


def get_sum(n, k):
    """ calculate sum of multiples of k till n """
    d = n // k
    return k * d * (d + 1) // 2


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    print(get_sum(n, 3) + get_sum(n, 5) - get_sum(n, 15))
