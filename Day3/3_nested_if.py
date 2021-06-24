print("Welcome to the rollercoaster")
height = input("Enter your height : ")
age = input("Enter your age : ")

# this is using the nested if and also elif can be used
if height > 120:
    print("you are cannot ride !")
    if age > 18:
        print("You are an adult.")
    else:
        print("You are a child.")
else:
    print("You can go on the rollercoaster")
    if age > 18:
        print("You can ride but you are an adult")
    else:
        print("You can ride also you are a child")
    