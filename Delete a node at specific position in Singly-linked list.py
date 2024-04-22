class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = None
    for data in arr:
        head = insertNodeAtEnd(head, data)
    return head

def insertNodeAtEnd(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()  

def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return head.next  
    curr = head
    index = 1
    while index != position - 1:  
        curr = curr.next
        index += 1
    mainNode = curr.next
    nextNode = mainNode.next
    
    mainNode.next = None
    curr.next = nextNode  
    return head


n = int(input())
data = list(map(int, input().split()))


head = createLinkedList(data)
printLinkedList(head)

position = int(input())
head = deleteNodeAtSpecificPosition(head, position)
printLinkedList(head)


