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


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val=0, next=None):
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
        while (current):
            print(current.val)
            current = current.next
    
    def mergeTwoLists(l1, l2):
        """
        First Approach Two pointers, head is pointing to prehead and prehead to a new ListNode. Let's iterate the list until both has the same  lenght,
        if value of list1 is lower than value of list2, header.next will be the lower value of list1, and if value of l2 is grather than
        value of l1 header.next will point list2. At the end of the iteration, head will point to the next value is where the final list will 
        start. If one list is grather than other, it will be linked to the head.next of the final list.
        ||======= Big O ======= ||
        - Time complexity : O(n) , where n is the  length of the list.
        - Space complexity: O(1)
        """
        prehead = ListNode()
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

print("Linked List FINAL")

node3 = LinkedList(None)
node3.head = LinkedList.mergeTwoLists(node1.head, node2.head)
node3.print()
