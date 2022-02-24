# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def mergeTrees(self, root1, root2):
        """
        Recursion: Check if both nodes are with values, if yes add values. if just node root1 has value return node root2
        Use recursion to add values for left and right side of the nodes.
        """
        result_tree = TreeNode()
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        result_tree.val = root1.val + root2.val
        
        result_tree.left = self.mergeTrees(root1.left, root2.left)
        result_tree.right = self.mergeTrees(root1.right, root2.right)
        
        return result_tree