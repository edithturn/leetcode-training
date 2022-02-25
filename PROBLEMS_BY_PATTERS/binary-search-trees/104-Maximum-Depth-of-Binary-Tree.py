def maxDepth(root):
    if root is None:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        
        return max(left, right) + 1
    