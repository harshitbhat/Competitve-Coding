from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # directed graph
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
    
    def bfs(self, src):
        visited = [False] * len(self.graph)
        
        
        queue = []
        
        queue.append(src)
        visited[src] = True
        
        curr = 0
        
        while curr < len(queue):
            front = queue[curr]
            curr += 1
            
            print(front, end = " ")
            
            for i in self.graph[front]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    g.bfs(2)
    
         
        