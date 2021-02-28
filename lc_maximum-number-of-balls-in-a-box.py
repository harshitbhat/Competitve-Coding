class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        countBalls = {}
        for i in range(lowLimit,highLimit+1):
            s = 0
            temp = i
            while temp != 0:
                s += temp % 10
                temp //= 10
            if s not in countBalls.keys():
                countBalls[s] = 1
            else:
                countBalls[s] += 1
        maxCount = 0
        # print(countBalls)
        for i in countBalls:
            maxCount = max(maxCount,countBalls[i])
        return maxCount
        