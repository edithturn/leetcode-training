# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
	if root is None:
		return 0
	else :
		# Compute the height of left and right subtree
		l_height = height(root.left)
		r_height = height(root.right)
		#Find the greater one, and return it
		if l_height > r_height :
			return l_height+1
		else:
			return r_height+1

def print_given_level(root, level):
	if root is None:
		return
	if level == 1:
		print(root.val,end = ',')
	elif level > 1 :
		print_given_level(root.left , level-1)
		print_given_level(root.right , level-1)

def level_order(root):
	print('[', end = '')
	h = height(root)
	for i in range(1, h+1):
		print_given_level(root, i)
	print(']')

class Solution:
	def sortedArrayToBST(selft, nums):
		def helper(left, right):
			# If node left is grater than node right, is not a valid BST
			if (left > right):
				return None
			# Get the element in the midle of the array
			mid = ( left + right )//2
			# If my array doesn't have element in middle, I will take the I'll take the immediate element right
			if ((left + right)%2):
				mid += 1
			#Recursive function
			root = TreeNode(nums[mid])
			root.left = helper(left, mid - 1)
			root.right = helper(mid + 1, right)
			return root 
		return helper(0, len(nums) - 1)
	
nums = [-10,-3,0,5,9]
obj = Solution()
bst = obj.sortedArrayToBST(nums)
level_order(bst)