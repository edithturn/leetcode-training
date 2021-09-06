# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr
    
    def hasCycle(self, head):
        slow = head
        fast = head.next

        if( slow == None or fast == None):
            return False

        while(fast != None and slow != None):
            slow = head.next
            fast = fast.next.next

            if(slow == fast):
                return True
        return False


# Test Cases
my_list = LinkedList()

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

