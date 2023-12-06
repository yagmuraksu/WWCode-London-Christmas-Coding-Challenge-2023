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

if __name__ == '__main__':
    print("Test Case 1")
    llist_items1 = [13,16]

    llist1 = SinglyLinkedList()

    for i in range(len(llist_items1)):
        llist1.insert_node(llist_items1[i])

    printLinkedList(llist1.head)

    print("Test Case 2")
    llist_items2 = [17, 19, 5, 12]

    llist2 = SinglyLinkedList()

    for i in range(len(llist_items2)):
        llist2.insert_node(llist_items2[i])

    printLinkedList(llist2.head)
