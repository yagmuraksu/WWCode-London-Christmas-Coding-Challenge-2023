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

def has_cycle(head):
    current_node = head
    next_node = head
    while(current_node != None and  next_node!= None and next_node.next != None):
        current_node = current_node.next
        next_node =  next_node.next.next
        if(current_node ==  next_node):
            return 1
    return 0
        

if __name__ == '__main__':

    tests = [[1],
            [1,2,3]]
    index_list = [-1,1]

    for k in range(len(tests)):
        index = index_list[k]

        llist_count = len(tests[k])

        llist = SinglyLinkedList()

        for j in range(llist_count):
            llist_item = tests[k][j]
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        print("Linked List:")
        print(tests[k],"with tail",tests[k][index_list[k]] )
        result = has_cycle(llist.head)
        result_str = lambda x: "Yes" if result == 1 else "No"
        print("Does the linked has cycle?:",result_str(result))
