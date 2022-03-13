'''
The problem can be solved using backtracking, 
that says take a path and start walking on it 
and check if it leads us to the destination vertex 
then count the path and backtrack to take another path. 
If the path doesn't lead to the destination vertex, discard the path. 
This type of graph traversal is called Backtracking.
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
    
    def countPathsUtil(self, src, dest, visited, pathCount):
        visited[src] = True

        if src == dest:
            pathCount[0] += 1
        
        else:
            i = 0
            while i < len(self.graph[src]):
                if not visited[self.graph[src][i]]:
                    self.countPathsUtil(self.graph[src][i], dest, visited, pathCount)
                i += 1
        
        visited[src] = False
    
    def countPaths(self, src, dest):
        visited = [False] * self.V

        pathCount = [0]

        self.countPathsUtil(src, dest, visited, pathCount)
        return pathCount[0]

if __name__ == '__main__':
    g = Graph(4)
    
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 2
    d = 3

    print(g.countPaths(s, d))