class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def printLinkedList(head):
    while(head):
        print(head.data)
        head = head.next

def getNode(llist, positionFromTail):
    num_of_elems = 0
    temp_node = llist
    while(temp_node != None):
        num_of_elems += 1
        temp_node = temp_node.next
    position = num_of_elems - positionFromTail
    counter = 0
    while(llist != None):
        if(counter == position-1):
            return llist.data
        else:
            llist = llist.next
            counter += 1

def removeDuplicates(llist):
    new_llist = llist
    
    while(new_llist.next != None):
        if(new_llist.data == new_llist.next.data):
            new_llist.next = new_llist.next.next
        else:
            new_llist = new_llist.next

    return llist

if __name__ == '__main__':
    print("Get Node from tail position tests".upper())
    tests_getnode = [[1],[3,2,1]]
    positions = [0,2]

    for i in range(len(tests_getnode)):

        llist1 = SinglyLinkedList()

        for j in range(len(tests_getnode[i])):
            llist1_item = tests_getnode[i][j]
            llist1.insert_node(llist1_item)
        
        print("Sorted Linked List")
        printLinkedList(llist1.head)
        print(f"Node value at tail position {positions[i]}:")
        print(getNode(llist1.head, positions[i]))

    print("\n")
    print("Remove Duplicate tests".upper())

    tests_remove_list = [[1,2,2,3,4],[3,3,3,4,5,5]]
    for i in range(len(tests_remove_list)):

        llist1 = SinglyLinkedList()

        for j in range(len(tests_remove_list[i])):
            llist1_item = tests_remove_list[i][j]
            llist1.insert_node(llist1_item)
        
        print("Sorted Linked List")
        printLinkedList(llist1.head)
        print("After removing duplicates:")
        printLinkedList(removeDuplicates(llist1.head))
