#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        while headA is not None:
            visited.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in visited:
                return headB
                break
            else:
                headB = headB.next
        return None

    def getIntersectionNodeII(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getSize(headA)
        lenB = self.getSize(headB)
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA