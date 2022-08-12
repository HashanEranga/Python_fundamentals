n = int(input())
setA = set(list(map(int, input().split())))

m = int(input())
setB = set(list(map(int, input().split())))

sortedSet = sorted(setA.union(setB).difference(setA.intersection(setB)))

for i in sortedSet:
    print(i)

# learned set operations 
# set union intersection and difference and add
