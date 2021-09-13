# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(l1, l2):
    """
    Using auxiliary node current starting with zero. Compare which is grater in l1 or l2. Update the current to the lower value in both of the list.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    head = ListNode(0)
    current = head
    
    while l1 and l2:
        if l1.val > l2.val:
            current.next = l2
            l2 = l2.next
        else:
            current.next = l1
            l1 = l1.next
            
        current = current.next
    current.next = l1 or l2
    return head.next