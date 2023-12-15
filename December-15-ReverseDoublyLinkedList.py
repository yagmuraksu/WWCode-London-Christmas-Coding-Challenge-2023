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

def printLinkedList(head):
    while(head):
        print(head.data)
        head = head.next

def reverse(llist):
    current_head = llist
    new_head = DoublyLinkedListNode(None)
    while(current_head != None ):
        new_head = current_head
        
        prev_node = current_head.prev
        next_node = current_head.next
        
        current_head.prev = next_node
        current_head.next = prev_node
        
        current_head = next_node
    
    return new_head
        

if __name__ == '__main__':
    tests = [[1,2,3,4],[2,3,4],[17,20,23,35,47]]

    for j in range(len(tests)):
        llist_count = len(tests[j])

        llist = DoublyLinkedList()

        for i in range(llist_count):
            llist_item = tests[j][i]
            llist.insert_node(llist_item)

        print(f"Test Case {j+1}:")
        print("Doubly Linked List:")
        printLinkedList(llist.head)
        llist1 = reverse(llist.head)
        print("Reverse Doubly Linked List:")
        printLinkedList(llist1)
