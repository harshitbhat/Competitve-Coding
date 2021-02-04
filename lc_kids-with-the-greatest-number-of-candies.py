# Question: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxCandies = max(candies)
        for i in range(0,len(candies)):
            if (candies[i] + extraCandies) < maxCandies:
                ans.append(False)
            else:
                ans.append(True)
        return ans