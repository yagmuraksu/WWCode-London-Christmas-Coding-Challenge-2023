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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):

    current_node = root

    if(current_node != None and (current_node.left != None or current_node.right != None)):
        counter_left = height(current_node.left)
        counter_right = height(current_node.right)

        if(counter_left > counter_right):
            counter_left += 1
            return counter_left
        else:
            counter_right += 1
            return counter_right
    else:
        return 0

tests =[[3,5,2,1,4,5,6,7],
        [15],
        [3,1,7,5,4]]
for j in range(len(tests)):
    tree = BinarySearchTree()
    t = len(tests[j])

    for i in range(t):
        tree.create(tests[j][i])
    print(f"Test Case {j+1}:")
    print("Binary tree array:")
    print(tests[j])
    print("Height of the binary tree:")
    print(height(tree.root))

