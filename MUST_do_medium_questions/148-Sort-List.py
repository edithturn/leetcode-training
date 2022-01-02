# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 4 -> 2 -> 1 -> 3
        if not head or not head.next:
            return head
        slow, fast = head, head
        previous = None
        while fast and fast.next:
            previous = slow  #2
            slow = slow.next #1
            fast = fast.next.next #none
        previous.next = None  
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        tmpList = ListNode(None)
        current = tmpList
        
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        return tmpList.next
        