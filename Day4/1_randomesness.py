# psedo random number generation 
# Mersen and twister is the method that the python is using for randomization. 

# python random module uses for random number generarions

import random

# randint(a,b) = generate a number between a and b including a and b

random_number = random.randint(1,10)
print(random_number)

import myModule

print(myModule.pi)

# generating float number 
float_random = random.random()
print(float_random)

love_score = random.randint(1,100)
print(f"Here your percentage of love : {love_score}%".format())