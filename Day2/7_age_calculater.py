# getting user input about the age in years
current__age = input("Enter your age(in years) : ")

# check : the age datatype
print(type(current__age))

# consider the age expected
expected__age = 90

# find the ages left to live
in__years = expected__age - current__age
in__months = in__years * 12
in__weeks = in__months * 4
in__days = in__months * 30

# print the final result in a single statement 
print("You have {} years to live, {} months to live, {} weeks to live and {} days to live".format(in__years, in__months, in__weeks, in__days))

