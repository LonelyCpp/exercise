"""
Check Permutation: Given two strings, write a method
to decide if one is a permutation of the other.
"""


def check_permutation(str1, str2):
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    print(check_permutation("abc", "bca"))
    print(check_permutation("abc", "abc"))
    print(check_permutation("asdfasdf", "asfsdfasdf"))
    print(check_permutation("", "fasdfasdf"))
    print(check_permutation("asdfasdf", "dsafafds"))
