# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def pairSum(head):
    """"
    Two-pointer approach. Saving values of the Linked List into a list.
    Use two pointers to compare twins and return the max value.       
    Big (O)
    * Time : O(n)
    * Space: O(n)
    """
    
    res = []
    tmpSum = float('-inf')
    while head:
        res.append(head.val)
        head = head.next
    slow,fast = 0, len(res) - 1
    while slow < fast:
        tmpSum = max(tmpSum, res[slow] + res[fast])
        slow += 1                
        fast -= 1

    return tmpSum
            