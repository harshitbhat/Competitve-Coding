class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        mySet = set()
        for i in range(0,len(s) - k + 1):
            mySet.add(s[i:i+k])
        
        return len(mySet) == 2 ** k
