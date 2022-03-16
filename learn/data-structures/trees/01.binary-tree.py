class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # For some of the problems
        self.next = None
        self.parent = None
        self.count = None

class BinaryTree:
    def __init__(self, nodes):
        self.root = None
        for data in nodes:
            self.insert(data)
    
    def insert(self, node_data):
        newNode = TreeNode(node_data)

        if self.root == None:
            self.root = newNode
        else:
            parent = None
            tempNode = self.root

            while tempNode:
                parent = tempNode
                if node_data < tempNode.data:
                    tempNode = tempNode.left
                else:
                    tempNode = tempNode.right
            
            if node_data <= parent.data:
                parent.left = newNode
            else:
                parent.right = newNode
    

    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)

    def preOrder(self, root):
        if not root:
            return
        
        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


tree1 = BinaryTree( [1, 3, 2, 4] )

tree1.inOrder(tree1.root)
print()
tree1.preOrder(tree1.root)
print()