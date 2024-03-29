#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    # main diagonal sum
    primarySum = 0
    for i in range(n):
        primarySum += arr[i][i]
    
    secondarySum = 0
    for i in range(n):
        secondarySum += arr[i][n - 1 -i]
    
    diff = primarySum - secondarySum
    if(diff<0):
        diff*=-1
    
    return diff

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
