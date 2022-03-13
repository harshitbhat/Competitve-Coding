# ---------------------------------------------------------------------------- #
#                                   Using DFS                                  #
# ---------------------------------------------------------------------------- #

# ------------------------------ Connected Graph ----------------------------- #
'''
DFS for a connected graph produces a tree. 
There is a cycle in a graph only if there is a back edge present in the graph. 
A back edge is an edge that is from a node to itself (self-loop) or 
one of its ancestors in the tree produced by DFS. 
'''

# ---------------------------- Disconnected Graph ---------------------------- #
'''
For a disconnected graph, Get the DFS forest as output. 
To detect cycle, check for a cycle in individual trees by checking back edges.
'''

# --------------------------------- Back Edge -------------------------------- #
'''
To detect a back edge, keep track of vertices currently in the recursion stack 
of function for DFS traversal. 
If a vertex is reached that is already in the recursion stack, 
then there is a cycle in the tree. 
The edge that connects the current vertex to the vertex in the recursion stack is a back edge. 
Use recStack[] array to keep track of vertices in the recursion stack.
'''

# ---------------------------------------------------------------------------- #
#                                Implementation                                #
# ---------------------------------------------------------------------------- #

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, src, dest):
        self.graph[src].append(dest)
    
    def isCycleUtil(self, node, visited, recStack):
        visited[node] = True
        recStack[node] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[node]:
            if visited[neighbour] == False:
                if self.isCycleUtil(neighbour, visited, recStack) == True:
                    return True
                elif visited[neighbour] == True:
                    return True
        
        recStack[node] = False
        return False

    def isCycle(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)

        for node in self.V:
            if visited[node] == False:
                if self.isCycleUtil(node, visited, recStack) == True:
                    return True
        
        return False