class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ansI = 0
            for j in range(0,len(nums)):
                if j != i and nums[j] < nums[i]:
                    ansI += 1
            ans[i] = ansI
        return ans