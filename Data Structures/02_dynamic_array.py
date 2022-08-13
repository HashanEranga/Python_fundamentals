#!/bin/python3

from ctypes import sizeof
import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    # create a dynamic array
    dynArr = []
    lastAnswer = 0

    # create other lists 
    for _ in range(n):
        newList= [] 
        dynArr.append(newList)
    
    # iterate through queries
    for query in queries:
        # print(query)
        # if query 1
        if(query[0]==1):
            # print(1)
            indexVal = (query[1]^lastAnswer) % n
            dynArr[indexVal].append(query[2])

        # if query 2
        else:
            # print(2)
            indexVal = (query[1]^lastAnswer) % n
            nextIndexVal = (query[2] % len(dynArr[indexVal]))
            lastAnswer = dynArr[indexVal][nextIndexVal]
            print(lastAnswer)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)

    # print("".join(map(str, result)))
    