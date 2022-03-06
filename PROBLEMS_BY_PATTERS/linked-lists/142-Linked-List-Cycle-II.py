def detectCycle(head):
    """
    Checking if there is a cycle, if there is a cicle make fast pointer slow and create a another pointer in the head, 
    compare values until they match. If they match return node
    """
    if not head or not head.next:
        return None
    
    slow, fast = head, head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next  
        if fast == slow:
            break
    else:
        return None
    intersection = head
    while intersection != fast:
        intersection = intersection.next
        fast = fast.next
        
    return intersection