class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        diff = len(set(candyType))
        n = len(candyType) 
        if n // 2 < diff:
            return n // 2
        else:
            return diff