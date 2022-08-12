n, m = input().split()
listA = list(map(int, input().split()))
setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))

# print(n,m,listA, setA, setB)

happy = 0

for i in listA:
    if(setA.__contains__(i)):
        happy+=1
    if(setB.__contains__(i)):
        happy-=1

print(happy)
