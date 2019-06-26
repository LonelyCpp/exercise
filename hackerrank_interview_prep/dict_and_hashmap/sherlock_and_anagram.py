"""
Two strings are anagrams of each other if the letters of one 
string can be rearranged to form the other string. Given a 
string, find the number of pairs of substrings of the string
that are anagrams of each other.
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    anagram_dict = dict()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            sorted_substr = ''.join(sorted(substr))
            if sorted_substr in anagram_dict:
                anagram_dict[sorted_substr] += 1
            else:
                anagram_dict[sorted_substr] = 1

    count = 0
    for anagram in anagram_dict:
        count += get_pair_count(anagram_dict[anagram])

    return count


def get_pair_count(n):
    if n < 2:
        return 0
    return math.factorial(n) / math.factorial(2) / math.factorial(n - 2)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(int(result))
