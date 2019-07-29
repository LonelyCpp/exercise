"""
You are given two strings S and T of the same length N. 
Your task is to convert the string S into T by doing 
some operations. In an operation, you can delete the 
first character of the string  and append any character 
at the end of the string. You are required to determine 
the minimum number of operations to convert S into T.
"""


def count_rotations(s1, s2):
    count = 0
    s1_list = list(s1)
    s2_list = list(s2)
    while s1_list != s2_list and len(s1_list) > 0:
        s1_list.pop(0)
        s2_list.pop()
        count += 1

    print(count)


if __name__ == '__main__':

    q = int(input())
    s1 = input()
    s2 = input()
    count_rotations(s1, s2)
