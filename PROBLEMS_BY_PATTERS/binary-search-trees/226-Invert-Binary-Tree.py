def invertTree(root):
    if root is None:
        return None
    if root.left or root.right:
        val = root.left
        root.left = root.right
        root.right = val
    invertTree(root.left)
    invertTree(root.right)
    
    return root
        