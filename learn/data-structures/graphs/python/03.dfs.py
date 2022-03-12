from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
    
    def dfs(self, src, visited = set()):
        
        visited.add(src)
        print(src, end=" ")

        for neighbour in self.graph[src]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)