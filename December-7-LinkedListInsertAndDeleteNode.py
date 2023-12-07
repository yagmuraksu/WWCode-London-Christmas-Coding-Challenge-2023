
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


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if(head == None):
        head = new_node
    else:
        tail_node = head
        while(tail_node.next != None):
            tail_node = tail_node.next
        tail_node.next = new_node
    
    return head

def insertNodeAtHead(llist, data):
    head_node = SinglyLinkedListNode(data)
    head_node.next = llist
    
    return head_node

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    current_node = llist
    idx = 0
    while( idx < position-1 ):
        current_node = current_node.next
        idx += 1
    next_node = current_node.next
    current_node.next = new_node
    new_node.next = next_node
    
    return llist

def deleteNode(llist, position):
    if(llist == None):
        return llist
    else:
        if(position == 0):
            llist = llist.next
        else:
            llist.next = deleteNode(llist.next,position-1)
            
    return llist

if __name__ == '__main__':
    print("Insert a node at the end of the linked list Test Case:")

    elements_to_add = [236,326,937]
    llist = SinglyLinkedList()

    for i in range(len(elements_to_add)):
        llist_item = elements_to_add[i]
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    printLinkedList(llist.head)

    print("Insert a node at the beginning of the linked list Test Case:")

    elements_to_add2 = [382,484,392,975,321]
    llist2 = SinglyLinkedList()

    for i in range(len(elements_to_add2)):
        llist_item = elements_to_add2[i]
        llist_head = insertNodeAtHead(llist2.head, llist_item)
        llist2.head = llist_head

    printLinkedList(llist2.head)

    print("Insert a node at the given position of the linked list Test Case:")

    elements_to_add3 = [16,13,7]
    llist3 = SinglyLinkedList()

    for i in range(len(elements_to_add3)):
        llist_item = elements_to_add3[i]
        llist3.insert_node(llist_item)

    data = 1
    position = 2

    llist_head = insertNodeAtPosition(llist3.head, data, position)
    printLinkedList(llist_head)

    print("Delete a node at the given position of the linked list Test Case:")

    elements_to_add4 = [20,6,2,19,7,4,15,9,3]
    llist4 = SinglyLinkedList()

    for i in range(len(elements_to_add4)):
        llist_item = elements_to_add4[i]
        llist4.insert_node(llist_item)

    position = 8

    llist_head = deleteNode(llist4.head, position)
    printLinkedList(llist_head)

