class Node:
    def __init__(self, data=None, next=None):
        self.data =data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("Liked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next 
        itr.next = Node(data, None)
    
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll =LinkedList()
    ll.insert_value(["edith", "pavel", "jean"])
    ll.print_linked_list()
