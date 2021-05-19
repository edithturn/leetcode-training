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

    def isPalindrome(self, head): 

        self.front_pointer = head
        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

# Creating the object to Linked List
my_list = LinkedList()

# Creating 03 nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)


my_list.head = node1
node1.next = node2
node2.next = node3 
node3.next = node4

#my_list.print_list()
print(my_list.isPalindrome(node1))
