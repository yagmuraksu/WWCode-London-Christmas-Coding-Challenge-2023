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

def reverseLinkedList(llist):
    prev_node = None
    curret_node = llist
    while(curret_node != None):
        next_node = curret_node.next
        curret_node.next = prev_node
        prev_node = curret_node
        curret_node = next_node
    llist = prev_node

    return llist

def printLinkedList(head):
    while(head):
        print(head.data)
        head = head.next

def reversePrint(llist):
    llist = reverseLinkedList(llist)
    printLinkedList(llist)

    return llist

if __name__ == '__main__':
    tests = [[16,12,4,2,5],[7,3,9],[5,1,18,3,13]]

    for j in range(len(tests)):
        llist_count = len(tests[j])

        llist = SinglyLinkedList()

        for i in range(llist_count):
            llist_item = tests[j][i]
            llist.insert_node(llist_item)

        print(f"Test {j+1}:")
        reversePrint(llist.head)