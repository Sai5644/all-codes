def insertNodeAtHead(llist, data):
    # Write your code here
        newBlock = SinglyLinkedListNode(data)
        if llist == None:
            return newBlock
        newBlock.next = llist 
        return newBlock
