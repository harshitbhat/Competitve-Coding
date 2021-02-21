# cook your dish here
import math

def solve(n,height,iq):
    dp = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if height[j] < height[i] and iq[j] > iq[i]:
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)

T = int(input())
while T > 0:
    T = T - 1
    n  = int(input())
    height = list(map(int,input().split()))
    iq = list(map(int,input().split()))
    print(solve(n,height,iq))
    
