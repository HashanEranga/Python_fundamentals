#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # total = 0
    maxim = -100000
    for i in range(4):
        for j in range(4):
            print(findHourGlassSum(i,j,arr))
            maxim = max(findHourGlassSum(i,j, arr), maxim)
            # total += 1
            # print()
    # print(total)
    return maxim

def findHourGlassSum(i, j, arr):
    glassSum = 0
    for k in range(3):
        for l in range(3):
            # print(arr[k+i][l+j],end=" ")
            # if ((k != 1 and l != 0) or  (k != 1 and l!= 2)):
            if (k==1 and l==0) or (k==1 and l==2):
                continue
            glassSum += arr[k+i][l+j]
            # remove the unnecessary values
        # print()
    return glassSum

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)