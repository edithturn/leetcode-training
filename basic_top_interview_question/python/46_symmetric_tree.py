# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Time complexity : O(n)O(n). Because we traverse the entire input tree once.
Space complexity : The number of recursive calls is bound by the height of the tree. In the worst case, the tree is linear and the height is in O(n)O(n).
"""
class Solution:
    """
    This function will check is the Tree is a mirror of itself
    """
    def isSymmetric(self, root):
        if (root == None):
            return True
        # Calling recursion function to check all the leaves, left against right in all the leaves all the Node
        return self.check_if_mirror(root.left, root.right)         
    
    """
    Pattern: Using recursion to check if node left is equal to node right. Root doesn't need to be compared beacuse is mirror itself
    """
    def check_if_mirror(self, node01, node02):
        # Is any node null and the other not so return False, if both are null return True
        if node01 == None or node02  == None:
            return node01 == node02
        # Checking if the value of the nodes are different, so return False
        if node01.val != node02.val:
            return False
        # Comparing if left of node01 and right of node02 are equal and if right node01 and left node02 are equal.
        # If they are it will return True
        return self.check_if_mirror(node01.left, node02.right) and self.check_if_mirror(node01.right, node02.left)
    """
    Pre Order traversal: Visit the root, Traverse the left subtree, Traverse the right subtree, . | Time Complexity: O(n) 
    """
    def postorderTraversal(self, root: None):
        if root is None:
            return []

        stack = [root]
        _list = []
        
        while stack:
            root = stack.pop()
            _list.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        print(_list[::-1])

    
    def preorderTraversal(self, root):
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            root = stack.pop()
            if root is not None:
                result.append(root.val)
                if root.left is not None:
                    stack.append(root.left)
                if root.right is not None:
                    stack.append(root.right)
        return result

            
# Creating a simetric mirror tree
node = TreeNode(1)
node.right = TreeNode(2)
node.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)

node.right.left.left = TreeNode(1)
node.right.left.right = TreeNode(5)

node.right.right.left = TreeNode(1)
node.right.right.right = TreeNode(4)

node.left.left.left = TreeNode(1)
node.left.left.right = TreeNode(4)

node.left.right.left = TreeNode(1)
node.left.right.right = TreeNode(5)

#              1
#        /           \   
#       2             2
#     /   \         /   \
#    3     4       4     3
#   / \   / \     / \   / \
#  1   4 1   5   1   5 1   4


# Creating a simetric mirror tree
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(2)
node1.right.left = TreeNode(4)
node1.right.right = TreeNode(3)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(4)

#      1
#    /   \   
#   2     2
#  / \   / \
# 3   4 4   3 



# False
print(Solution().preorderTraversal(node))
print(Solution().isSymmetric(node))

# True
print(Solution().preorderTraversal(node1))
print(Solution().isSymmetric(node1))