class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        j = 1
        ans = nums[i]
        tempAns = ans
        while j < len(nums):
            if nums[j] > nums[j-1]:
                tempAns += nums[j]
                j += 1
            else:
                i += 1
                ans = max(ans,tempAns)
                tempAns = nums[i]
                j = i + 1
        ans = max(ans,tempAns)
        return ans