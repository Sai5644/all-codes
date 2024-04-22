class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

def enQueue(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock 
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock
    return head
 
def deQueue(head):
    # This function deletes first node
    if head == None:
        print("Queue is empty, nothing to delete")
        return None
 
    print( head.data)
    secondNode = head.next 
    head.next = None 
    return secondNode
 
def printQueue(head):
    if head == None:
        print("Queue is empty")
        return 
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()

n = int(input())
head = None

for _ in range(n):
    op = input().split()
    if op[0] == '1':
        head = enQueue(head, int(op[1]))
        print(op[1], "inserted")
    elif op[0] == '2':
        if head is not None:
            print(head.data)
        else:
            print("Queue is empty")
    elif op[0] == '3':
        head = deQueue(head)
    elif op[0] == '4':
        printQueue(head)
    elif op[0] == '5':
        if head is None:
            print("Queue is empty")
        else:
            print("Queue is not empty")
