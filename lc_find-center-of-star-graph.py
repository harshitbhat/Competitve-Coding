from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        ans = -1
        maxLen = -1
        for i in graph:
            if len(graph[i]) > maxLen:
                maxLen = len(graph[i])
                ans = i
        return ans