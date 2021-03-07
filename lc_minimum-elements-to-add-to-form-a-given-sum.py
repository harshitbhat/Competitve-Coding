class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        ans = 0
        sumArray = sum(nums)
        while sumArray != goal:
            if sumArray > goal:
                diff = sumArray - goal
                if abs(diff) <= limit:
                    sumArray += (abs(diff) * -1)
                    ans += 1
                else:
                    times = abs(diff) // limit
                    sumArray += (times * limit * -1)
                    ans += times
            else:
                diff = goal - sumArray
                if diff <= limit:
                    sumArray += diff
                    ans += 1
                else:
                    times = diff // limit
                    sumArray += times * limit
                    ans += times
            
        return ans