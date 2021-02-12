class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        temp = []
        while i < len(s):
            temp.append(s[i])
            curr = 1
            j = i+1
            while j < len(s):
                if s[j] not in temp:
                    temp.append(s[j])
                    curr += 1
                    j += 1
                else:
                    break
            ans = max(ans,curr)
            i += 1
            while temp:
                temp.pop()
                
        return ans