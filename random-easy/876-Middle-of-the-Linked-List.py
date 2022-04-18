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


        
def middleNode(head):
    """
    Two Pointers: slow and fast, move one faster pointer every two nodes
    until it finds the end of the Linked List, so we are putting a slow pointer
    in the middle of the LinkedList and it is the node to return.
    1 -> 2 -> 3 -> 4 -> 5 : It returns 3
    1 -> 2 -> 3 -> 4: It returns 3 second middle node.

    Big O
    =====
    Time: O(N), we are visiting each node of the Linked List one time.
    Space: O(1), no extra space is needed to solve this problem.
    """
    if head.next == None:
        return head            
    slow, fast = head, head        
    while fast.next:
        slow = slow.next
        fast = fast.next.next            
        if fast == None or fast.next == None:
            return slow