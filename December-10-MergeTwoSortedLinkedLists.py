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

def mergeLists(head1, head2):
    sorted_ll = sorted_head = SinglyLinkedListNode(0)

    while(head1 != None and head2 != None):
        if(head1.data < head2.data):
            sorted_ll.next = head1
            head1 = head1.next
        else:
            sorted_ll.next = head2
            head2 = head2.next
            
        sorted_ll = sorted_ll.next
        
    if(head1 != None):
        sorted_ll.next = head1
    if(head2 != None):
        sorted_ll.next = head2
        
    return sorted_head.next

if __name__ == '__main__':
    tests = [[[1,2,3],[3,4]],
            [[4,5,6],[1,2,10]]]

    for i in range(len(tests)):

        llist1 = SinglyLinkedList()

        for j in range(len(tests[i][0])):
            llist1_item = tests[i][0][j]
            llist1.insert_node(llist1_item)

        llist2 = SinglyLinkedList()

        for j in range(len(tests[i][1])):
            llist2_item = tests[i][1][j]
            llist2.insert_node(llist2_item)
        
        print("Sorted Linked List 1")
        printLinkedList(llist1.head)
        print("Sorted Linked List 2:")
        printLinkedList(llist2.head)
        print("Merged Linked List:")
        printLinkedList(mergeLists(llist1.head, llist2.head))

