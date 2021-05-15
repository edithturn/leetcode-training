# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class LinkedList:
    """
    two-pointer technique.
    """
    def print_list(self):
        _list = self.head
        while _list is not None:
            print(_list.val)
            _list = _list.next

# Creating the object to Linked List
my_list = LinkedList()

# Creating 03 nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)


my_list.head = node1
node1.next = node2
node2.next = node3 
node3.next = node4
#node4.next = node2

my_list.print_list()
