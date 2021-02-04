T = int(input())
while T > 0:
    T = T - 1
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    sum1 = 0
    sum2 = 0
    for i in a:
        sum1 += i
    for i in b:
        sum2 += i
    ans = 0
    i = 0
    j = m-1
    while True:
        if sum1 > sum2:
            break
        if i >= n or j < 0:
            break
        sum1 += b[j] - a[i]
        sum2 += a[i] - b[j]
        i = i + 1
        j = j - 1
        ans = ans + 1
    if sum1 > sum2:
        print(ans)
    else:
        print(-1)