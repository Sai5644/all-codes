class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def deleteAtEndOfTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    previous = None
    while curr.next != None:
        previous = curr
        curr = curr.next
    previous.next = None
    return head

def deleteAtHead(head):
    if head is None:
        return None
    return head.next

n = int(input())
l = list(map(int, input().split()))


head = Node(l[0])
temp = head
for ele in l[1:]:
    temp.next = Node(ele)
    temp = temp.next


printLinkedList(head)
head = deleteAtHead(head)

printLinkedList(head)
