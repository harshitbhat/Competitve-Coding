import math
T = int(input())
while T > 0:
    T = T - 1
    n , k = map(int,input().split())
    ans = 0
    if k <= n:
        if n % k == 0:
            ans = math.ceil(k/n)
        else:
            ans = math.ceil(k/n) + 1
    else:
        ans = math.ceil(k/n)
    print(ans)