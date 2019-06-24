"""
It's New Year's Day and everyone's in line for the Wonderland
rollercoaster ride! There are a number of people queued up,
and each person wears a sticker indicating their initial
position in the queue. Initial positions increment by 1 from 1
at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front
of them to swap positions. If two people swap positions, they
still wear the same sticker denoting their original places in
line. One person can bribe at most two others. For example, if
n = 8 and P5 bribes P4 , the queue will look like this:
[1, 2, 3, 5, 4, 6, 7, 8].

Fascinated by this chaotic queue, you decide you must know the
minimum number of bribes that took place to get the queue into
its current state!
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

#!/bin/python3


def minimumBribes(q):
    q.insert(-99999999999999999999999, 0)
    count = 0
    for index, person in enumerate(q):
        diff = person - index
        if diff > 2:
            print("Too chaotic")
            return

        for j in range(max(1, person - 1), index):
            if q[j] > person:
                count += 1

    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
