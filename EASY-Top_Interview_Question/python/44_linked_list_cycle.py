# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class LinkedList:
    """
    two-pointer technique.
    """
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr
    def hasCycle(self, head):
        llist = set()
        current = self.head
        while current:
            if current in llist:
                return True
            llist.add(current)
            current = current.next
        return False

    def print_list(self):
        _list = self.head
        while _list is not None:
            print(_list.val)
            _list = _list.next

# Creating the object to Linked List
my_list = LinkedList()

# Creating 03 nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)


my_list.head = node1
node1.next = node2
node2.next = node3 
node3.next = node4
pos = 1
node4.next = my_list.get_node(my_list.head, pos)

#my_list.print_list()
print(my_list.hasCycle(my_list.head))
