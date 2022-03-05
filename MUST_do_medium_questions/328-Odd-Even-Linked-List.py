# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(head):
        """
        Using two pointer, one for even an other other odd. Keep traking the numbers in the same time.
        Big O:
        Time: O(1)
        Space: O(n)
        """
        if not head :
            return head
        even_head = head.next
        
        odd = head
        even = head.next
        
               
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        return head
        
            
            