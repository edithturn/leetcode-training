# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		newNode = Node(data)
		if(self.head):
			current = self.head
			while(current.next):
				current = current.next
			current.next = newNode
		else:
			self.head = newNode

	def printLL(self):
		current = self.head
		while(current):
			print (current.data)
			current = current.next

	def reverseList(self):
		previous = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous

LL =  LinkedList()
LL.insert (3)
LL.insert (4)
LL.insert (5)
LL.insert (6)
LL.printLL()
print("After reversed node")
LL.reverseList()
LL.printLL()