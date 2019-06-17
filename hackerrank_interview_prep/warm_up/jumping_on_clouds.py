"""
Emma is playing a new mobile game that starts with 
consecutively numbered clouds. Some of the clouds are 
thunderheads and others are cumulus. She can jump on 
any cumulus cloud having a number that is equal to the 
number of the current cloud plus 1 or 2. She must avoid 
the thunderheads. Determine the minimum number of jumps 
it will take Emma to jump from her starting postion to 
the last cloud. It is always possible to win the game.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = 0
    current_pos = 0
    while(current_pos < len(c)):
        if current_pos == len(c) - 1:
            break
        if current_pos + 2 >= len(c):
            jumps += 1
            break
        else:
            jumps += 1
            if c[current_pos + 2] is 0:
                current_pos += 2
            else:
                current_pos += 1
    return jumps


if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
