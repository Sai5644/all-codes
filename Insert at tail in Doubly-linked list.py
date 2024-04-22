class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtEndOfTail(tail, data):
    new_node = Node(data)
    if tail is None:
        return new_node
    tail.next = new_node
    new_node.prev = tail
    return new_node

def printLinkedListLeftToRight(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def printLinkedListRightToLeft(tail):
    curr = tail
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()

n = int(input())
elements = list(map(int, input().split()))
new_number = int(input())

head = None
tail = None
for ele in elements:
    tail = insertAtEndOfTail(tail, ele)
    if head is None:
        head = tail



printLinkedListLeftToRight(head)
printLinkedListRightToLeft(tail)

tail = insertAtEndOfTail(tail, new_number)

printLinkedListLeftToRight(head)
printLinkedListRightToLeft(tail)
