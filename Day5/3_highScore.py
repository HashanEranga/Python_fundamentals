marksList = input("Marks list add here : ").split()
marksList_int = [int(mark) for mark in marksList]

# print(marksList, marksList_int)
maxMark = marksList_int[0]
for marks in marksList_int:
    if marks > maxMark:
        maxMark = marks

print(maxMark)