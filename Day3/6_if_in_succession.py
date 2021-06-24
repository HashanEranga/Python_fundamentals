print("Welcome to the rollercoaster")
height = int(input("What is the height :"))

if height > 120:
    print("You cannot enter")
else:
    print("you can enter")

reply = str(input(" if you want a photo : Y or N "))
if reply == "Y" :
    print("Photo charge is taken.")
else:
    print("Charge for photo not taken")

# use logical operators for if and else conditions