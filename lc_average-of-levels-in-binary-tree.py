# My initial Solution
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = []
        levels = []
        queue.append([0,root])
        while queue:
            if queue[0][1].left:
                queue.append([queue[0][0] + 1,queue[0][1].left])
            if queue[0][1].right:
                queue.append([queue[0][0] + 1,queue[0][1].right])
            popped = queue.pop(0)
            levels.append([popped[0],popped[1].val])
        levels.sort()
        print(levels)
        maxLevels = -1
        for i in levels:
            maxLevels = max(maxLevels,i[0])
        ans = [[] for i in range(maxLevels+1)]
        for i in levels:
            ans[i[0]].append(i[1])
        for i in range(0,len(ans)):
            ans[i] = sum(ans[i])/len(ans[i])
        return ans

# Better Solution
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        queue = []
        queue.append(root)
        while queue:
            nextLevel = []
            levelSum = 0
            for i in queue:
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
                levelSum += i.val
            ans.append(levelSum/len(queue))
            queue = nextLevel
        return ans
