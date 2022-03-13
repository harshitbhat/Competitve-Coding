from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, src, dest):
        self.graph[src] = dest
        self.graph[dest] = src

    def isCyclicUtil(self, node, visited, parent):
        visited[node] = True

        for i in self.graph[node]:
            if not visited[i]:
                if self.isCyclicUtil(i, visited, node):
                    return True
            elif parent != i:
                return True
        
        return False
    
    def isCyclic(self):
        visited = [False] * (self.V)

        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicUtil(i, visited, -1):
                    return True
        
        return False