n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
toCheck = {}
for i in range(1,n+1):
    toCheck[i] = False
for i in range(1,a[0]+1):
    toCheck[a[i]] = True
for i in range(1,b[0]+1):
    toCheck[b[i]] = True
isPossible = True
for i in range(1,n+1):
    if toCheck[i] == False:
        isPossible = False
        break
if isPossible == True:
    print('I become the guy.')
else:
    print('Oh, my keyboard!') 