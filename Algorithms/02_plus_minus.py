#!/bin/python3

from ast import FormattedValue
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    neg = 0
    zero = 0

    for i in arr:
        if(i>0):
            plus+=1
        elif(i<0):
            neg+=1
        else:
            zero+=1
    
    plusRatio = plus/len(arr)
    negRatio = neg/len(arr)
    zeroRatio = zero/len(arr)

    print("{:.6f}".format(plusRatio))
    print("{:.6f}".format(negRatio))
    print("{:.6f}".format(zeroRatio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
