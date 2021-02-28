class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        toSelect = []
        for i in baseCosts:
            toSelect.append(i)
        for i in toppingCosts:
            first = len(toSelect)
            for j in range(0,first):
                toSelect.append(toSelect[j] + 0 * i)
                toSelect.append(toSelect[j] + 1 * i)
                toSelect.append(toSelect[j] + 2 * i)
        toSelect.sort()
        if target in toSelect:
            return target
        
        diff = 99999999999
        ans = -1
        for i in toSelect:
            if abs(i-target) < diff:
                diff = abs(i-target)
                ans = i
        return ans
                