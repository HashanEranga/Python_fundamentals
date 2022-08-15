#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(time):
    # Write your code here
    h, m, s = map(int, time[:-2].split(':'))
    p = time[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return (h,m,s)
if __name__ == '__main__':

    s = input().strip()

    result = timeConversion(s)
    print(('%02d:%02d:%02d') % result)

