class Solution:
    
    def longestNiceSubstring(self, s: str) -> str:
        def checkNice(hash):
            isPossible = True
            for i in hash:
                if (i.lower() in hash.keys()) and (i.upper() in hash.keys()):
                    isPossible = True
                else:
                    isPossible = False
                    break
            return isPossible
    
        ans = []
        for i in range(0,len(s)):
            myHash = {}
            myHash[s[i]] = True
            for j in range(i+1,len(s)):
                myHash[s[j]] = True
                if checkNice(myHash) == True:
                    ans.append([i,j])
        req = -1
        low = -1
        high = -1
        if len(ans) == 0:
            return ''
        for i in ans:
            if (i[1] - i[0]) > req:
                req = i[1] - i[0]
                final = s[i[0]:i[1]+1]
        return final