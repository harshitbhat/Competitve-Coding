# Question: https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append(nums[i] + ans[i-1])
        return ans