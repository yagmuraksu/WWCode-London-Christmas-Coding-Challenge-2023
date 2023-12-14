class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def sortedInsert(llist, data):
    
    new_node = DoublyLinkedListNode(data)
    current_node = llist

    if(current_node == None):
        current_node = new_node
    elif(current_node.data >= data):
        new_node.next = current_node
        current_node.prev = new_node
        current_node = new_node
        llist = current_node
    else: #data>current_node.data
        while(current_node.next != None and current_node.next.data < new_node.data):
            current_node = current_node.next
        new_node.next = current_node.next
        
        if(current_node.next !=None):
            current_node.prev = new_node
        
        current_node.next = new_node
        new_node.prev = current_node
    
    return llist

def printLinkedList(head):
    while(head):
        print(head.data)
        head = head.next

if __name__ == '__main__':

    tests = [[1,3,4,10],[2,3,4],[1,2,3]]
    nodes = [5,1,4]

    for j in range(len(tests)):
        llist_count = len(tests[j])

        llist = DoublyLinkedList()

        for i in range(llist_count):
            llist_item = tests[j][i]
            llist.insert_node(llist_item)

        data = nodes[j]

        llist1 = sortedInsert(llist.head, data)

        print(f"Test {j+1}:")
        print("Sorted Doubly Linked List:")
        print(tests[j])
        print(f"Node to be inserted: {nodes[j]}")
        print("New Doubly Linked List:")
        printLinkedList(llist1)