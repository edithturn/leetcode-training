
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeNodes(head):
    
    resultList = ListNode(0)
    pointer = resultList
    nodeSum = 0
    while head:
        if head.val == 0:
            if nodeSum != 0:
                pointer.next = ListNode(nodeSum)
                pointer = pointer.next
                nodeSum = 0
        else:
            nodeSum += head.val
            
        head = head.next
            
    return resultList.next


def mergeNodes(head):
    """
    Traverse the entire linked list, and with another "pointer"
    to a new linked list save the sum of nodes of the previous linked list
    with values greater than zero.
    Big (O):
    * Time : O(n)
    * Space: O(1)    
    """
    newList = ListNode(0)
    pointer = newList
    
    while head and head.next:
        if head.val == 0:
            head = head.next
            nodesum = 0
            while head.val > 0:
                nodesum += head.val
                head = head.next
            pointer.next = ListNode(nodesum)
            pointer =pointer.next
            
    return newList.next