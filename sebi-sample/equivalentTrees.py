class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class Tree:
    def __init__(self, nodes):
        self.root = None
        for data in nodes:
            self.insert(data)
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        parent = None
        temp = self.root

        while temp:
            parent = temp
            if data <= temp.data:
                temp = temp.left
            else:
                temp = temp.right
        
        if data <= parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
    
def inOrder(root):
    if not root:
        return
        
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

def depth(root):
    if not root:
        return 0
    
    return 1 + max(depth(root.left), depth(root.right))

def areEquivalent(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False
    
    return areEquivalent(root1.left, root2.left) and areEquivalent(root1.right, root2.right)

n = int(input())

mainTree = list(map(int, input().split()))

mainTree = Tree(mainTree[:-1])

for i in range(n - 1):
    tree = list(map(int, input().split()))
    tree = Tree(tree[:-1])

    if areEquivalent(mainTree.root, tree.root):
        print(f'YES {abs( depth(mainTree.root) - depth(tree.root) )}')
    else:
        print(f'NO {abs( depth(mainTree.root) - depth(tree.root) )}')
