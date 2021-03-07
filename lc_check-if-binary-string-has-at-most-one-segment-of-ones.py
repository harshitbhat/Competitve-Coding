class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if (len(s) == 1):
            return True
        for i in range(0,len(s)):
            if s[0:i+1] == '1' * len(s[0:i+1]) and s[i+1:len(s)] == '0'* len(s[i+1:len(s)]):
                return True
        return False