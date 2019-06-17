"""
Gary is an avid hiker. He tracks his hikes meticulously, 
paying close attention to small details like topography. 
During his last hike he took exactly n steps. 
For every step he took, he noted if it was an uphill, U ,
or a downhill, D step. Gary's hikes start and end at sea 
level and each step up or down represents a 1 unit change 
in altitude. 
We define the following terms:

A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step 
down to sea level.
A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up 
to sea level.
Given Gary's sequence of up and down steps during his last hike, 
find and print the number of valleys he walked through.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    level = 0
    valley_count = 0
    for ch in s:
        if ch is 'D':
            level -= 1
            if level is -1:
                valley_count += 1
        else:
            level += 1
    return valley_count


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
