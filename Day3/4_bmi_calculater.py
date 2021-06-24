print("BMI Calculater")
height = float(input("Enter Your Height : "))
weight = float(input("Enter your weight : "))


# BMI value
bmi = round(weight/height**2, 2)

# print the states
if bmi < 18.5:
    print("Your BMI is {} Under Weight".format(bmi))
elif bmi < 25:
    print("Your BMI is {} Normal Weight".format(bmi))
elif bmi < 30:
    print("Your BMI is {} Over Weight".format(bmi))
elif bmi < 35:
    print("Your BMI is {} Obese".format(bmi))
elif bmi > 35:
    print("Your BMI is {} Clinically Obese".format(bmi))
else:
    print("Invalid Input.")
