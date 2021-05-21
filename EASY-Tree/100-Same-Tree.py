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


node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)

node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.right = TreeNode(3)

node3 = TreeNode(1)
node3.left = TreeNode(4)
node3.right = TreeNode(3)


obj = Solution()
print(obj.isSameTree(node1, node3))