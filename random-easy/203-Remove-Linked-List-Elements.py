# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(head, val):
        
        prev = None
        current = head
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                    head = current.next
                current = current.next                
            else:
                prev = current
                current = current.next
            
        return head