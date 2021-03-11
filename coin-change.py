import sys
def coinChange(coins,amount):
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0
    
    coins.sort()
    for i in range(1,amount+1):
        for c in range(0,len(coins)):
            if (i-coins[c]) < 0:
                break
            if dp[i-coins[c]] != sys.maxsize:
                dp[i] = min(dp[i], 1 + dp[i-coins[c]])
    
    if dp[amount] == sys.maxsize:
        return -1
    return dp[amount]


arr = [186,419,83,408]
amount = 6249

print(coinChange(arr,amount))