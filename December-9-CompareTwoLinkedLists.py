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

def compare_lists(llist1, llist2):
    equality = 1

    while(llist1 != None and llist2 != None):
        if(llist1.data != llist2.data):
            equality = 0
        llist1 = llist1.next
        llist2 = llist2.next
    
    if((llist1 == None and llist2 != None) or (llist1 != None and llist2 == None)):
        equality = 0

    return equality


if __name__ == '__main__':
    tests = [[[2,1],[2,1,1]],
             [[2,1,2],[2,1,2]]]

    for i in range(len(tests)):

        llist1 = SinglyLinkedList()

        for j in range(len(tests[i][0])):
            llist1_item = tests[i][0][j]
            llist1.insert_node(llist1_item)

        llist2 = SinglyLinkedList()

        for j in range(len(tests[i][1])):
            llist2_item = tests[i][1][j]
            llist2.insert_node(llist2_item)

        print("Linked List 1")
        printLinkedList(llist1.head)
        print("Linked List 2:")
        printLinkedList(llist2.head)
        print("Result:")
        print(compare_lists(llist1.head, llist2.head))
