import sys
T = int(input())
while T > 0:
    T = T - 1
    n , x = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * n
    sumArr = 0
    for i in range(0,n):
        sumArr += a[i]
        count = 0
        z = a[i]
        while z % x == 0:
            count += 1
            z = z//x
        b[i] = count
    minIndex = 0
    for i in range(1,n):
        if b[i] < b[minIndex]:
            minIndex = i
    ans = sumArr * (b[minIndex] + 1)
    i = 0
    while i < minIndex:
        ans += a[i]
        i += 1
    print(ans)
    