# Works fine but n,m are <= 3000 so will not work for large m,n
def largestMerge1(word1,word2):
    m = len(word1)
    n = len(word2)
    dp = [['' for i in range(n)] for j in range(m)]
    dp[0][0] = max(word1[0]+word2[0],word2[0]+word1[0])
    for i in range(1,n):
        dp[0][i] = max(dp[0][i-1] + word2[i],word2[0:i+1]+word1[0])
    for i in range(1,m):
        dp[i][0] = max(dp[i-1][0] + word1[i],word1[0:i+1]+word2[0])
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = max(dp[i-1][j] + word1[i], dp[i][j-1] + word2[j])
    # print(dp)
    return dp[m-1][n-1]

def largestMerge(word1,word2):
    ans = ''
    while word1 and word2:
        if word1>word2:
            ans += word1[0]
            word1 = word1[1:]
        else:
            ans += word2[0]
            word2 = word2[1:]
    ans += word1
    ans += word2
    return ans

print(largestMerge('abcabc','abdcaba'))