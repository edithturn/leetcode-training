# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

 
def isPalindromeI(head):
    """
    Brute Force: Traverse the Linkedlist and add its items to a list.
    Then with Two Pointers compare the left and right indices
    to know if it is a palindrome.
    Bit(O)
    ===========
    Time : O(n)
    Space: O(n)
    """
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    
    left = 0
    right = len(arr) - 1
    
    while right >= left:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeII(head):
    """
    Pattern: Find the middle of the Linked List. 
    Reverse half of the Linked List,
    then compare the values with Two Pointers 
    to see if they are palindorme.
    Bit(O)
    ===========
    Time : O(n)
    Space: O(1)    
    """
    slow, fast = head, head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    current = slow
    previous = None
    lnext = None
    
    while current:
        lnext = current.next
        current.next = previous
        previous = current
        current = lnext
    
    left, right = head, previous
    
    while right:
        if left.val != right.val:
            return False
        else:
            left = left.next
            right = right.next
    return True


