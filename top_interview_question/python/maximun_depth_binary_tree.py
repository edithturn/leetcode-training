class Node:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

def maxSize(root):
	if root == None:
		return 0

	leftSize = maxSize(root.left)
	rightSize = maxSize(root.right)

	if leftSize > rightSize:
		return leftSize + 1
	else:
		return rightSize  + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node (4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.left = Node(8)
print ("Max Size deph is :" , maxSize(root))