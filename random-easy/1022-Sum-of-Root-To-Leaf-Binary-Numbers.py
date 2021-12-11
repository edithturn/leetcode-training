# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Usign recursion: If the node doesn't have left and right, concatenate the last value of the node into a string.
        Then add the number in base two to the total.
        Big O:
        - time:  O(n), since we are iterating each node once
        - Space: O(1), not extra memory is needed. There is just tmp variable and the stack itselve
        """
       
        self.sum = 0        
        
        def helper(root, nums):
            
            if root.left == None and root.right == None:
                nums += str(root.val)
                self.sum += int(nums, 2)
                return
            
            nums += str(root.val)
            
            if root.left != None:
                helper(root.left, nums)
                
            if root.right != None:            
                helper(root.right, nums)
            
                    
        helper(root, "")
        return self.sum
    
   
        
    
            
        