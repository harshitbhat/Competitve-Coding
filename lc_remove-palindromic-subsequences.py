class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(s,l,r):
            i = l
            j = r
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if len(s) == 0:
            return 0
        if isPalindrome(s,0,len(s)-1):
            return 1
        return 2
