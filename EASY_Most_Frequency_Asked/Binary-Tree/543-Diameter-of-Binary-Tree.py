# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:

#        1
#      /   \
#     2     3
#    / \
#   4   5


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        """      
        First Approach using recursion and a auxiliar function: high = 1 + max(left, right) and diameter = left + right + 2
        ||======= Big O ======= ||
        * Time complexity : O(n)
        * Space complexity: O(n)
        """        
        maxDiameter = [0]

        def getDiameter(root):
            if not root:
                return -1
            left = getDiameter(root.left)
            right = getDiameter(root.right)
            
            maxDiameter[0] = max(maxDiameter[0], left + right + 2)
            
            return 1 + max(left, right)
        
        getDiameter(root)
        return maxDiameter[0]

# Test Cases
#root = [1,2,3,4,5]
#        1
#      /   \
#     2     3
#    / \
#   4   5

if	__name__ == "__main__":
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	res = Solution().diameterOfBinaryTree(root)
	print (res)