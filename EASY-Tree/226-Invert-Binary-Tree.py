# Definition for a binary tree node.
class TreeNode:
    """
    This function initialize the Node with attributes of val, left, rigth
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Function call swap function to make a recursive swap in the nodes left and right
        At the end we return the Tree
        """
        self.swap(root)
        return root
    
    def swap(self, current: TreeNode):
        """
        Function will take a node and inspect right and left nodes
        Creating a temporal variabel to swap the nodes
        Recursive function to swap starting for the first left side
        """
        if current == None:
            return 0
        self.swap(current.left)
        self.swap(current.right)
        
        tmp   = current.left
        current.left  = current.right
        current.right = tmp

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode (1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print ("Max Size deph is :" , Solution.invertTree(root))

"""
==> Optimized Approach <==
To solve this exercise I used RECURSION, for each node we will swap the values. 
After swap we return to the previous node to check with other node.

==> Time / Space Complexity <==
Time: O(2^n) where "n" is the number of nodes of the Tree
Space: O(n)
"""