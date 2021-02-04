def max(a,b):
    if a > b:
        return a
    else:
        return b
dp = {}

def coins(n):
    if n <= 3:
        return n
    try:
        return dp[n]
    except:
        dp[n] = max(n,coins(int(n/2)) + coins(int(n/3)) + coins(int(n/4)))
        return dp[n]

while True:
    try:
        n = int(input())
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        print(coins(n))
    except:
        break