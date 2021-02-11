class Solution:
    def maxArea(self, height: list[int]) -> int:
#        O(n^2)
        ans = -1
        for i in range(0,len(height)):
            for j in range(i,len(height)):
                ans = max(ans,min(height[i],height[j]) * (j-i))
        return ans

    def maxArea2(self, height: list[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            if height[i] <= height[j]:
                ans = max(ans, (height[i]) * (j-i) )
                i += 1
            else:
                ans = max(ans, (height[j]) * (j-i) )
                j -= 1
        return ans 