T = int(input())
while T > 0:
    T = T - 1
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(0,n):
        ans = ans + a[i] * b[i]
    print(ans)