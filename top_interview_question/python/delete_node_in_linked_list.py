class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
	
class LinkedList:
	def __init__(self):
		self.head = None

	def	insert(self, data):
		newNode =Node(data)
		if(self.head):
			current = self.head
			while(current.next):
				current = current.next
			current.next = newNode
		else:
			self.head = newNode

	def	printLL(self):
		current = self.head
		while(current):
			print(current.data)
			current = current.next

	def	deleteNode(self, data):
		current = self.head
		while(current):
			if (current.data == data) :
				current.data = current.next.data
				current.next = current.next.next
			current = current.next
		
LL =  LinkedList()
LL.insert (3)
LL.insert (4)
LL.insert (5)
LL.insert (6)
LL.printLL()
print("After deleted node")
LL.deleteNode(5)
LL.printLL()