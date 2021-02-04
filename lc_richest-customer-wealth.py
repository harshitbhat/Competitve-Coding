# Question: https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = -1
        for i in accounts:
            wealth = 0
            for j in i:
                wealth += j
            ans = max(ans,wealth)
        return ans