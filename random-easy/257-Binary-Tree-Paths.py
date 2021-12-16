# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:       
        _list = []
        path =""
        def helper(root, path):
            if root == None:
                return            
            if root.left == None and root.right == None:
                _list.append(path+str(root.val))
            if root.left:
                helper(root.left, path +str(root.val)+"->")
            if root.right:
                helper(root.right, path +str(root.val)+"->")
        
        helper(root, "")
        return _list
