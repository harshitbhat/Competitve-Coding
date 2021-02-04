T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    a = list(map(int,input().split()))
    intim = [False] * n
    for i in range(1,n-1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            intim[i] = True
        elif a[i - 1] > a[i] and a[i] < a[i + 1]:
            intim[i] = True
    maxCons = [0] * n
    total = 0
    for i in range(0,n):
        if intim[i] == True:
            total += 1
            if intim[i-1] == True:
                maxCons[i] = maxCons[i-1] + 1
            else:
                maxCons[i] = 1
    maxInt = -1
    for i in maxCons:
        if i > maxInt:
            maxInt = i

    if maxInt >= 3:
        total -= 3
    elif maxInt == 2:
        total -= 2
    elif maxInt == 1:
        total -= 1
    print(total)
        

    

