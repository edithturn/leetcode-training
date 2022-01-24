#         self.next = next
def deleteDuplicates(head):
    if not head:
        return None
    current = head
    while current:
        if current.next and current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Test Cases
# head = [1,1,2] output [1,2] 
# head = [1,1,2,3,3] output [1,2,3]
