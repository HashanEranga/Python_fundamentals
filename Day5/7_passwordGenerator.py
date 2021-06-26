import random

# data generation
# textFile = open("symbols.txt", 'w')
# for a in range(33,48):
#     textFile.write(str(a) + "\n")
# for a in range(58,65):
#     textFile.write(str(a) + "\n")
# for a in range(91,97):
#     textFile.write(str(a) + "\n")
# for a in range(123,127):
#     textFile.write(str(a) + "\n")
# textFile.close()

# textFile = open('letters.txt', 'w')
# for a in range(65,91):
#     textFile.write(str(a) + "\n")
# for a in range(97,123):
#     textFile.write(str(a) + "\n")
# textFile.close()

# textFile = open('numbers.txt', 'w')
# for a in range(48,58):
#     textFile.write(str(a) + "\n")
# textFile.close()

symbolList = []
letterList = []
numberList = []

textFile = open('symbols.txt', 'r')
for symbol in textFile:
    symbolList.append(chr(int(symbol.strip("\n"))))
textFile.close()

textFile = open('letters.txt', 'r')
for symbol in textFile:
    letterList.append(chr(int(symbol.strip("\n"))))
textFile.close()

textFile = open('numbers.txt', 'r')
for symbol in textFile:
    numberList.append(chr(int(symbol.strip("\n"))))
textFile.close()

numLetters = int(input("Enter the number of letter to be in your password : "))
numSymbols = int(input("Enter the number of symbols to be in your password : "))
numNumbers = int(input("Enter the number of numbers to be in your password : "))

randomLetters = random.choices(letterList, k = numLetters)
randomSymbols = random.choices(symbolList, k = numSymbols)
randomNumbers = random.choices(numberList, k = numNumbers)

easyVersionPwd = randomNumbers + randomLetters + randomSymbols
easyStringPwd = ''.join([str(a) for a in easyVersionPwd])
print(easyStringPwd)

random.shuffle(easyVersionPwd)
print("This is the easy password " + easyStringPwd)
hardStringPwd = ''.join([str(a) for a in easyVersionPwd])
print("This is the hard password " + hardStringPwd)