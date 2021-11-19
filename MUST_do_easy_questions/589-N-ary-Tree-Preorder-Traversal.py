"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def preorder(root):
    
    """Pre order: root-left-right
    Recursion: if node has data add into the list, then iterate each children in the node to check if the node has date (recursion) and add into the list.
    Repeating this for each node in the tree.
    Big O:
    Time: O(n), each node is iterating once
    Space: O(n), using stack in the recursion
    """
    ans = []
    
    def recursion(node):
        
        if node is not None:
            ans.append(node.val)
        else:
            return ans
        
        for n in node.children:
            recursion(n)
            
    recursion(root)
    
    return ans
    
    
            
        