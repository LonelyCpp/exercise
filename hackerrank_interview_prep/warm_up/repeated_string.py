"""
Lilah has a string, s, of lowercase English letters 
that she repeated infinitely many times.Given an 
integer, n, find and print the number of letter a's 
in the first  letters of Lilah's infinite string.

For example, if the string s = 'abcac' and n = 10, 
the substring we consider is 'abcacabcac', the first 
10 characters of her infinite string. There are 4 
occurrences of a in the substring.
https://www.hackerrank.com/challenges/repeated-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    if 'a' in s:
        init_count = s.count('a')
        repetions = n // len(s)
        base_count = init_count * repetions

        extra_str = s[0:n % len(s)]
        total_count = base_count + extra_str.count('a')
        return total_count
    else:
        return 0


if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
