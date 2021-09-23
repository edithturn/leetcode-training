# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Using recursion to swap values of left and right. get left, get right, then processes and retur to the father node
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    def invertTree(self, root):
        self.swap(root)
        return root
    
    def swap(self, root):
        if root is None:
            return 
        self.swap(root.left)
        self.swap(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp


# Test Cases
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode (1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

pp = Solution()
pp.invertTree(root)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
print(root.right.right.val)

