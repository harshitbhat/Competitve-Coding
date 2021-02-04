# Question: https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        ans = nums[-k:] + nums[0:]
        for i in range(0,k):
            ans.pop()
        for i in range(0,len(nums)):
            nums[i] = ans[i]