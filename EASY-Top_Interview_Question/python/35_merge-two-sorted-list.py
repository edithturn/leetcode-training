def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
    prehead = ListNode()
    head = prehead

    while l1 and l2:
        d1 = l1.val
        d2 = l2.val
        
        if d1 <= d2:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
        
    if l1:
        head.next = l1
    if l2:
        head.next = l2

    return prehead.next
                
                