# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1
# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2
# 1 -> 2
# 2 -> 3

# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: [] 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class LinkedList():
    """
    First Approach Two pointers for "reverseList"

    ||======= Big O ======= ||
    - Time complexity : O(n) , where n is the  length of the list.
    - Space complexity: O(1)
    """
    def __init__(self):
        self.head = None

    def insert(self, val):
        newNode = ListNode(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print(self):
        current = self.head
        while(current):
            print (current.val)
            current = current.next

    def reverseList(self, node):
        current = self.head
        previous  = None

        while (current != None):
            temporal = current.next
            current.next = previous
            previous = current
            current = temporal
        self.head = previous


# Test Cases

node = LinkedList()

node.insert (3)
node.insert (4)
node.insert (5)
node.insert (6)
node.print()
print("After reversed node")
node.reverseList(node)
node.print()