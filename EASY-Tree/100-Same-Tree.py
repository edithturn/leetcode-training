# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example 01 
# Input: p = [1,2,3], q = [1,2,3]
#      1         1
#    /   \     /   \
#   2     3   2     3
#
# Output: true
# Example 02
# Input: p = [1,2], q = [1,null,2]
#     1    1
#    /      \
#   2        2
# Output: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left) == True and self.isSameTree(p.right, q.right) == True:
            return True
        return False


# O(n^2)

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)

node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.right = TreeNode(3)

node3 = TreeNode(1)
node3.left = TreeNode(5)



obj = Solution()
print(obj.isSameTree(node1, node3))