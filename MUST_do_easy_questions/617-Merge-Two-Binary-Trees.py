# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Recursion to traverse the tree, and adding the value of root01 to root2 in root3, just in case both trees have date.
    ||======= Big O ======= ||
    Time complexity : O(nm), where n is lenght of root1 and m is lenght of root2
    Space complexity: O(max(len(m, n))
    """
    def mergeTrees(self, root1, root2):
        root3 = TreeNode()
        if root1 and root2:
            root3.val = root1.val + root2.val
            root3.left = self.mergeTrees(root1.left, root2.left)
            root3.right = self.mergeTrees(root1.right, root2.right)
            return root3
        else:
            return root1 or root2



# Test Cases

#root1 = [1,3,2,5]
#root2 = [2,1,3,null,4,null,7]
#root3= [3,4,5,5,4,null,7]