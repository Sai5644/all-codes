class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtEndOfhead(head, data):
    new_node = Node(data)
    if head == None:
        return new_node
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = new_node
    new_node.prev = tail
    return head

def printLinkedListLeftToRight(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def printLinkedListRightToLeft(tail):
    curr = tail
    while curr.next is not None:
        curr = curr.next
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()



    
def addNodeAtHeadOfLinkedList(head, data):
    new_node = Node(data)
    if head == None:
        return new_node
   
    new_node.next = head 
    head.prev = new_node
    return new_node

n = int(input())
elements = list(map(int, input().split()))
new_number = int(input())

head = None
for ele in elements:
    head = insertAtEndOfhead(head, ele)

printLinkedListLeftToRight(head)
printLinkedListRightToLeft(head)

head = addNodeAtHeadOfLinkedList(head, new_number)

printLinkedListLeftToRight(head)

tail = head
while tail.next != None:
    tail = tail.next

printLinkedListRightToLeft(tail)
