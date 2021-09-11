# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        Using two pointers: Iterate both linked list and, get the lenght. Look the difference and iterate both list until they reach an equal point, return that intersection.
        ||======= Big O ======= || 
        Time complexity : O(n)
        Space complexity: O(1)
        """
        currA,currB  = headA, headB
        lenA, lenB = 0

        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        
        currA, currB = headA, headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                currA = currA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                for i in range(lenB-lenA):
                    currB = currB.next
        while(currA != currB):
            currA = currA.next
            currB = currB.next
        
        return currA