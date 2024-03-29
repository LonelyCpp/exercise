"""
Harold is a kidnapper who wrote a ransom note,
but now he is worried it will be traced back to
him through his handwriting. He found a magazine
and wants to know if he can cut out whole words
from it and use them to create an untraceable
replica of his ransom note. The words in his note
are case-sensitive and he must use only whole words
available in the magazine. He cannot use substrings
or concatenation to create the words he needs.

Given the words in the magazine and the words in
the ransom note, print Yes if he can replicate his
ransom note exactly using whole words from the magazine;
otherwise, print No.

For example, the note is "Attack at dawn". The magazine
contains only "attack at dawn". The magazine has all
the right words, but there's a case mismatch.
The answer is NO.
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""
#!/bin/python3


def check_magazine(magazine, note):
    mag_dict = dict()
    for word in magazine:
        if word in mag_dict:
            mag_dict[word] += 1
        else:
            mag_dict[word] = 1

    for word in note:
        if word in mag_dict and mag_dict[word] is not 0:
            mag_dict[word] -= 1
        else:
            print("no")
            return

    print("yes")


if __name__ == '__main__':

    MAG = input().rstrip().split()

    NOTE = input().rstrip().split()

    check_magazine(MAG, NOTE)
