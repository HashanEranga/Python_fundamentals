# print the initial message
print("Welcome to the tip calculater !")

# asking the total bill
total__bill = input("What was the total bill ? ")

# asking the percentage of the tip 
tip__percent = input("What percentage tip would you like to give ? 10, 12 or 15 ? ")

# asking the no of peoples to split the bill 
no__of__people = input("How many people to split the bill ? ")

# # validate each value and the type of each value
# print(total__bill, tip__percent, no__of__people)
# print(type(total__bill), type(tip__percent), type(no__of__people))

# calculate the answer for calculate the bill final and price per each one 
actual__bill__amount = total__bill * (tip__percent/100 + 1)
charge__per__one =  actual__bill__amount/no__of__people

# Display price per one 
print("Charge per one person = {}".format(charge__per__one))