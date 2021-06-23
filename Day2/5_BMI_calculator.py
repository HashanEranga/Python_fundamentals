# Getting the input of the users weight & height
weight, height = int(input("What is the weight : ")), int(input("What is the height : "))

# print the values recieved for confirmation
# print(weight, height)

# calculate the BMI value 
BMI = float(weight)/float(height)**2

# checked the type of the variable
# print(type(BMI))

# # prints the number for clarify the answer
# print(BMI)

# Print the BMI value
print("The value of your BMI = %0.2f" %BMI)