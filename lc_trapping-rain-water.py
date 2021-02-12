class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        for i in range(0,len(height)):
            maxL = maxR = 0
            if height[0:i]:
                maxL = max(height[0:i])
            else:
                maxL = 0
            if height[i:]:
                maxR = max(height[i:])
            else:
                maxR = 0
            ans += max(min(maxL,maxR) - height[i],0)
        return ans