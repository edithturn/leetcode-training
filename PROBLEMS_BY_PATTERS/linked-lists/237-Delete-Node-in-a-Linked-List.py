# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        Replace the value of the node we wnat to replace with the value of its next node
        then connect the node with the next nodes.
        """
        replace = node.next
        node.val = replace.val
        node.next = replace.next
        