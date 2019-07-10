"""
Given a string, write a function to check if it
is a permutation of a palin­ drome. A palindrome
is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement
of letters. The palindrome does not need to be
limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

from collections import Counter


def permu_pal(string):
    length = len(string)
    count = Counter(string)
    odd_flag = False

    for c in count:
        if count[c] % 2 == 0:
            continue

        if length % 2 == 0:
            return False

        if not odd_flag:
            odd_flag = True
        else:
            return False

    return True


print(permu_pal("abccba"))
print(permu_pal("abcba"))
print(permu_pal("abcfba"))
print(permu_pal("aaaaa"))
print(permu_pal("aaaaav"))
print(permu_pal("aaaaavv"))
