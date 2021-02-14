class Solution:
    def minOperations(self, s: str) -> int:
        a1 = 0
        for i in range(0,len(s)):
            if i % 2 == 0:
                if s[i] != '1':
                    a1 += 1
            else:
                if s[i] != '0':
                    a1 += 1
        a2 = 0
        for i in range(0,len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    a2 += 1
            else:
                if s[i] != '1':
                    a2 += 1
        return min(a1,a2)