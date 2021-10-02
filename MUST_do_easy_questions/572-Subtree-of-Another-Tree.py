# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Using recursion. When values of each node are equal, compare left and right until reach null in both nodes (Line 27)
    ||======= Big O ======= ||
    Time complexity : O(mn), where n is the lenght in node s and m is the lenght in the node in t
    Space complexity: O(min(mn))
    """
    def isSubtree(self, root, subRoot):
        if root == None:
            return False
        elif self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def isSameTree(self, s, t):
        if(s == None or t == None):
            return s == None and t == None
        elif s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:
            return False