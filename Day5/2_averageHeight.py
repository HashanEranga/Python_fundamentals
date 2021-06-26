student_heights_lists = input("Enter the student heights : ").split()
count = 0
sum = 0
for student in student_heights_lists:
    count +=1
    sum += int(student)

average = format(sum/count, ".2f")
print("Students Average height : {}".format(average))
