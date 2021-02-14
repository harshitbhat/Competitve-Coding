def solve(mat):
    dp = []
    for row in mat:
        temp = [0 for i in range(len(row))]
        dp.append(temp)
    n = len(mat)
    dp[0][0] = mat[0][0]
    for i in range(1,n):
        dp[i][0] = mat[i][0] + dp[i-1][0]
    for i in range(1,n):
        dp[i][i] = mat[i][i] + dp[i-1][i-1]
    if n > 2:
        for i in range(2,n):
            for j in range(1,i):
                dp[i][j] = mat[i][j] + max(dp[i-1][j],dp[i-1][j-1])
    ans = dp[0][0]
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            ans = max(ans,dp[i][j])
    
    return ans

T = int(input())
while T:
    T = T - 1
    n = int(input())
    mat = []
    for i in range(n):
        s = list(map(int,input().split()))
        mat.append(s)
    print(solve(mat))