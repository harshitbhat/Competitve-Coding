s,n = map(int,input().split())
arr = []
for i in range(n):
    fight = list(map(int,input().split()))
    arr.append(fight)
isPossible = True
arr.sort()
for i in arr:
    x = i[0]
    y = i[1]
    if x < s:
        s = s + y
    else:
        isPossible = False
        break
if isPossible == True:
    print('YES')
else:
    print('NO')