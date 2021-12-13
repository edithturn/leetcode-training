# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, tmpSum, targetSum):
            if root == None:
                return False
            tmpSum += root.val
            if tmpSum == targetSum and root.left == None and root.right == None:
                return True
            return helper(root.left, tmpSum, targetSum) or helper(root.right, tmpSum, targetSum)
        
        return helper(root, 0, targetSum)            
                 
