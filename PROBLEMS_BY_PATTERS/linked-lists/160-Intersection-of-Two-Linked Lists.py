def getIntersectionNode(headA, headB):
    
    node01 = headA
    node02 = headB
    
    while  node01 != node02:

        if node01:
            node01 = node01.next
        else:
            node01 = headB

        if node02:
            node02 = node02.next
        else:
            node02 = headA
    
    return node02