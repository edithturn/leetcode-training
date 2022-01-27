def middleNode(head):
    """
    Brute Force
    """
    if head == None:
        return None
    count = 0
    current = head
    while current:
        current = current.next
        count +=1
    
    middle = (count//2)
    current = head
    while middle > 0 and current:
        middle -= 1
        current = current.next
    return current
        
    
def middleNode( head):
    """
    Fast and Slow pointer
    """
    if head == None:
        return None
    fast, slow = head, head
    
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
        else:
            break
            
        slow = slow.next
    
    return slow
        