def isSubSetSum(arr,n,k):
    subset = ([[False for i in range(k+1)] for i in range(n+1)])

    for i in range(n+1):
        subset[i][0] = True
    
    for i in range(1,k+1):
        subset[0][i] = False

    for i in range(1,n+1):
        for j in range(1,k+1):
            if j < arr[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= arr[i-1]:
                subset[i][j] = subset[i-1][j] or subset[i-1][j-arr[i-1]]
    
    return subset[n][k]

T = int(input())
while T > 0:
    T = T - 1
    x,k = map(int,input().split())
    powArr = []
    i = 0
    while (k**i) < 10e18:
        powArr.append(k**i)
        i += 1
    length = len(powArr)
    if isSubSetSum(powArr,len(powArr),x) == True:
        print('YES')
    else:
        print('NO')