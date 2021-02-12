class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st = -1
        en = -1
        for i in range(0,len(nums)):
            if nums[i] == target:
                st = i
                break
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == target:
                en = i
                break
            i -= 1
        return [st,en]