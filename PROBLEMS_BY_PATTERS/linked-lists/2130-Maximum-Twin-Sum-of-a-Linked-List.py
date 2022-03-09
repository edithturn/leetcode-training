# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        """
        Saving the values of the nodes into an array. Then two pointers to calculate the sum of the nod eand its twin. Each time looking for the max twin.
        """
        arr = []
        tmp = head
        maxx = float('-inf')
        
        while head:
            arr.append(head.val)
            head = head.next
        
        slow, fast = 0, len(arr) - 1
        while slow < fast:
            maxx = max(maxx, arr[slow] + arr[fast])
            slow += 1
            fast -= 1
            
        return maxx