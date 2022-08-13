# getting a 2d array
from array import array


arr = []
n = 12
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

# reading a number integer
n = int(input().strip())

# getting space separated inputs
arr = list(map(int, input().rstrip().split()))

# getting two inputs and make them int
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
q = int(first_multiple_input[1])

# create a dynamic array
dynArr = []
# lastAnswer = 0

# create other lists 
for _ in range(n):
    newList= [] 
    dynArr.append(newList)
