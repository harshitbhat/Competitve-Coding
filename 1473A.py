T = int(input())
while T > 0:
    T = T - 1
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    isPossible = False
    areAllLess = True
    for i in arr:
        if i > m:
            areAllLess = False
            break
    if areAllLess == False:
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] + arr[j] <= m:
                    isPossible = True
                    break
            if isPossible == True:
                break
    else:
        isPossible = True
    if isPossible == True:
        print('YES')
    else:
        print('NO')
    