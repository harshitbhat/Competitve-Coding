# cook your dish here
import math
T = int(input())
while T > 0:
    T = T - 1
    n , k  = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        print(0)
    else:
        a.sort()
        ans = 10e10
        i = 0
        while (i + k - 1) < n:
            ans = min(ans,a[i+k-1] - a[i])
            i += 1
        print(ans)
