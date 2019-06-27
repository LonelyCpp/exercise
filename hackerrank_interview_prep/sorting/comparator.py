"""
Comparators are used to compare two objects. In this challenge, 
you'll create a comparator and use it to sort an array. The 
Player class is provided in the editor below. It has two fields:

name : a string.
score : an integer.

Given an array of  Player objects, write a comparator that sorts 
them in order of decreasing score. If 2 or more players have the 
same score, sort those players alphabetically ascending by name.
https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
"""

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name + " " + self.score

    def comparator(a, b):
        if a.score == b.score:
            if a.name < b.name:
                return -1
            if a.name > b.name:
                return 1
            return 0

        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
