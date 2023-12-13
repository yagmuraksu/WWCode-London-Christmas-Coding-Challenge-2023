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

def findMergeNode(head1, head2):
    while(head2 != None):
        temp_node = head1
        while(temp_node  != None):
            if(temp_node == head2): 
                return temp_node.data
            temp_node = temp_node.next
        head2 = head2.next
    return None

if __name__ == '__main__':
    tests = [[1,2,3],[1]],[[1,2,3],[1]]
    intersection_node = [1,2]

    for j in range(len(tests)):
        index = intersection_node[j]

        llist1_count = len(tests[j][0])

        llist1 = SinglyLinkedList()

        for i in range(llist1_count):
            llist1_item = tests[j][0][i]
            llist1.insert_node(llist1_item)
            
        llist2_count = len(tests[j][1])

        llist2 = SinglyLinkedList()

        for i in range(llist2_count):
            llist2_item = tests[j][1][i]
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        print("Linked List 1:",tests[j][0])
        print("Linked List 2:",tests[j][1])
        result = findMergeNode(llist1.head, llist2.head)
        print("Merge node: ",result)