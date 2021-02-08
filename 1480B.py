import math
T = int(input())
while T > 0:
    T = T - 1
    A, B , n = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    powerPair = []
    for i in range(0,n):
        powerPair.append([a[i],b[i]])
    powerPair.sort()
    ansCheck = [False for i in range(n)]
    remainPower = B
    for i in range(n):
        if remainPower <= 0:
            break
        x = math.ceil(powerPair[i][1] / A)
        y = math.ceil(remainPower / powerPair[i][0])
        if y < x:
            break
        remainPower -= x * powerPair[i][0]
        ansCheck[i] = True
    if False in ansCheck:
        print('NO')
    else:
        print('YES')