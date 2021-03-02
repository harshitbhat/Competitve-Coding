class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        n = len(nums)
        nums.sort()
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                dup = nums[i]
                break
        return [dup, (n * (n+1)) // 2 - sum(nums) + dup]