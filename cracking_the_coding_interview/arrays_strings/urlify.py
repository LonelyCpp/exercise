"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""


def trim(string):
    """re-implement the trim function for fun"""

    # left trim
    left_space_count = 0
    for char in string:
        if char == ' ':
            left_space_count += 1
        else:
            break

    string = string[left_space_count:]

    # right trim
    right_space_count = 0
    for i in range(len(string) - 1, 0, -1):
        if string[i] == ' ':
            right_space_count += 1
        else:
            break

    if right_space_count:
        string = string[0:-right_space_count]

    return string


def urlify(string):
    trimmed_str = trim(string)
    return trimmed_str.replace(' ', '%20')


print("'", urlify("  Mr John Smith     "), "'", sep='')
