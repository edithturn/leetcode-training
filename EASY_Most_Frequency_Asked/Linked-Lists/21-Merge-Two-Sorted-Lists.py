# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

#  Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]



#class ListNode:
#    """
#    Definition for singly-linked list.
#    """
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = None
        self.val = val
        self.next = next

    def insert(self, val):
        newNode = LinkedList(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def print(self):
        current = self.head
        while (current):
            print(current.val)
            current = current.next
    
    def mergeTwoLists(self, l1, l2):
        prehead = LinkedList()
        head = prehead
        
        while l1 and l2:
            value1 = l1.val
            value2 = l2.val
            
            if value1 <= value2:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            
            head = head.next
            
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        
        return prehead.next
            
# Test Cases
l1 = [1,2,4]
l2 = [1,3,4]


node1 = LinkedList()
node1.insert(1)
node1.insert(2)
node1.insert(4)

node2 = LinkedList()
node2.insert(1)
node2.insert(3)
node2.insert(4)

print("Linked List 01")
node1.print()
print("Linked List 02")
node2.print()

object = LinkedList()
node3 = None
print("Linked List FINAL")
#node3 = object.mergeTwoLists(node1, node2)
#node3.print()

node3 = LinkedList.mergeTwoLists(self, node1, node2)
node3.print()

#print("My final Linked List")
#node3.print()