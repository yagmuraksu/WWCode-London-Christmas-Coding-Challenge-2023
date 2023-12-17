class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)

tests =[[1,2,5,3,6,4],
        [1,14,3,7,4,5,15,6,13,10,11,2,12,8,9]]
for j in range(len(tests)):
    tree = BinarySearchTree()
    t = len(tests[j])

    for i in range(t):
        tree.create(tests[j][i])
    print(f"Test Case {j+1}:")
    print("Tree array:")
    print(tests[j],'\n')
    print("Tree's postorder traversal values:")
    postOrder(tree.root)
    print("\n")
    print("Tree's inorder traversal values:")
    inOrder(tree.root)
    print("\n")