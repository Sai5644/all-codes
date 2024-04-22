class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None
        
def insertAtEndOfTail(tail, data):
    new_node = Node(data)
    if tail is None:
        return new_node
    tail.next = new_node
    new_node.prev = tail
    return new_node

def printLeftToRightManner(head):
    curr = head
    while curr !=None:
        print(curr.data,end=" ")
        curr = curr.next
    print()

def printRightToLeftManner(tail):
    curr = tail
    while curr !=None:
        print(curr.data,end=" ")
        curr = curr.prev
    print()

n = int(input())
l = list(map(int, input().split()))

# Creating the doubly linked list
head = None
tail = None
for ele in l:
    tail = insertAtEndOfTail(tail, ele)
    if head is None:
        head = tail

# Printing in left to right manner
printLeftToRightManner(head)

# Printing in right to left manner
printRightToLeftManner(tail)
