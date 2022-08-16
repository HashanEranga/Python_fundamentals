#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def roundNearestFive(grade, base=5):
    return base * round(grade / base)


def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for grade in grades:
        modGrade = roundNearestFive(grade)
        if (modGrade > grade) and ((modGrade - grade) < 3) and (modGrade >= 40):
            # print(modGrade)
            newGrades.append(modGrade)
        else:
            # print(grade)
            newGrades.append(grade)
    return newGrades


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    results = gradingStudents(grades)
    for result in results:
        print(result)
