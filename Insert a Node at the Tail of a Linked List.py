def insertNodeAtTail(head, data):
        new_node = SinglyLinkedListNode(data)
        if head == None:
            return new_node
        curr = head 
        while curr.next!= None:
            curr = curr.next
        curr.next = new_node
        return head

