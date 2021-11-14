# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def trimBST(self, root, low, high):
    """
    Recursion: Discard evaluate left side in case root.val is lower than low.
    Discard evaluate right side if root.val is grather than high.
    If we reach the last node evaluate if the left and right node are in the low and high range.

    Big O:
    Time : O(n), where n is the number of nodes of the tree, visiting  a ode each time
    Space: O(n), where n is the call stack of the recursion
    """    
    def trim(root):
        if root is None:
            return None
        elif root.val > high:
            return trim(root.left)
        elif root.val < low:
            return trim(root.right)
        else:
            root.left = trim(root.left) 
            root.right = trim(root.right)
            return root
    return trim(root)
            
        
            