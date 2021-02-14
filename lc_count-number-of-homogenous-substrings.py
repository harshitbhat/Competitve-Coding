class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1000000007
        ct = [0] * len(s)
        ct[0] = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                ct[i] = ct[i-1] + 1
            else:
                ct[i] = 1
        ans = 0
        for i in ct:
            ans = ( ans + i) % mod
        return ans