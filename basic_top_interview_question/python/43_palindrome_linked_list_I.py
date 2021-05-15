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
            print (_list.val)
            _list = _list.next

    def isPalindrome(self, head: ListNode) -> bool:
        node_to_list = []
        current = head
        while head is not None:
            node_to_list.append(head.val)
            head = head.next
        return node_to_list == node_to_list[::-1]

# Creating the object to Linked List
my_list = LinkedList()

# Creating 03 nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(5)


my_list.head = node1
node1.next = node2
node2.next = node3 
node3.next = node4

#my_list.print_list()
print(my_list.isPalindrome(node1))
