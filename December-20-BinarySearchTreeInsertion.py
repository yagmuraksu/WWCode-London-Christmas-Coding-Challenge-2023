class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    #Node is defined as
    #self.left (the left child of the node)
    #self.right (the right child of the node)
    #self.info (the value of the node)

    def insert(self, val):
        if(self.root != None):
            current_node = self.root
            temp_node = current_node
            while(current_node != None):
                temp_node = current_node
                if(current_node.info > val):
                    current_node = current_node.left
                else:
                    current_node = current_node.right
                        
            current_node = temp_node
            if(current_node.info > val):
                current_node.left = Node(val)
            else:
                current_node.right = Node(val)
        else:
            self.root = Node(val)
        
        return self

tree = BinarySearchTree()

arr = [4,2,1,3,7,6]

for i in range(len(arr)):
    tree.insert(arr[i])

preOrder(tree.root)
