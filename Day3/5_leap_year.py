# take the year as an input 
# this is taken using logics 
year = input("Enter the year : ")

if (year % 4 == 0) and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0))):
    print("Leap Year")
else:
    print("Not a leap year")
    