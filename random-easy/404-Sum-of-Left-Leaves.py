# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumOfLeftLeaves(root):
    
    self.finalSum = 0 

    def sumOfLeftLeavesHelper(root):

        if root == None:
            return 0
        
        if root != None and root.left != None and(root.left.left == None and root.left.right == None):
            self.finalSum += root.left.val
        sumOfLeftLeavesHelper(root.left)
        sumOfLeftLeavesHelper(root.right)

    sumOfLeftLeavesHelper(root)
        
    return self.finalSum