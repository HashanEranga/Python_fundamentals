import random
inputString = input("Enter comma separated names here : ")
listOfNames = inputString.split(", ")
print(listOfNames)
randomPersonNumber = random.randint(1, len(listOfNames))
print(listOfNames[randomPersonNumber-1])

# altername method
print(random.choice(listOfNames))