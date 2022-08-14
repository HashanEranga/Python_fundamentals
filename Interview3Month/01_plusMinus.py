#!/bin/python3

import math
import os
import random
import re
import sys
# from turtle import pos

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arrLen = len(arr)
    posCount = 0
    negCount = 0
    zeroCount = 0

    for item in arr:
        if(item > 0):
            posCount+=1
        elif(item < 0):
            negCount+=1
        else:
            zeroCount+=1

    print("{:.6f}".format(posCount/arrLen))
    print("{:.6f}".format(negCount/arrLen))
    print("{:.6f}".format(zeroCount/arrLen))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
