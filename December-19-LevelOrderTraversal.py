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
def levelOrder(root):
    if(root != None):
        nodes = []
        nodes.append(root)
        while(len(nodes) != 0):
            current_node = nodes.pop(0)
            
            if(current_node.left != None):
                nodes.append(current_node.left)
            if(current_node.right != None):
                nodes.append(current_node.right)
                
            print(current_node.info, end=" ")


tree = BinarySearchTree()

arr = [1,2,5,3,6,4]

for i in range(len(arr)):
    tree.create(arr[i])

print("Level order traversal tree:")
levelOrder(tree.root)