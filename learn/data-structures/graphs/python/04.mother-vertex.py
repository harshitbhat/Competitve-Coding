from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
    
    def dfs(self, src, visited):
        visited.add(src)

        for node in self.graph[src]:
            if node not in visited:
                self.dfs(node, visited)
    
    def findMother(self):
        visited = set()

        v = 0

        for i in range(self.V):
            if i not in visited:
                self.dfs(i, visited)
                v = i

        # If there exist mother vertex (or vertices) in given
        # graph, then v must be one (or one of them)
 
        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.
 
        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.

        if any(node not in visited for node in range(self.V)):
            return -1
        return v


if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print ("A mother vertex is " + str(g.findMother()))