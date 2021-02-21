class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for i in range(0,len(boxes)):
            dist = 0
            for j in range(i+1,len(boxes)):
                if boxes[j] == '1':
                    dist += (j-i)
            ans[i] = dist
        i = len(boxes) - 1
        while i >= 0:
            j = i-1
            dist = 0
            while(j>=0):
                if boxes[j] == '1':
                    dist += (i-j)
                j -= 1
            ans[i] += dist
            i -= 1
        return ans