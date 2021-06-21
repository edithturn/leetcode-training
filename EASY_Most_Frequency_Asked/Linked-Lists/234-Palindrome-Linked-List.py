# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false


# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    """
    First Approach: add the linked list into a simple list, then iterate again to compare the first element with the last, 
    then return true just it reach the mittle and they are equals.
    ||======= Big O ======= ||
    - Time complexity : O(n) , where n is the  length of the list.
    - Space complexity: O(1)
    """
    def __init__(self, val=0, next=None):
        self.head = None
    
    def isPalindrome(self, head):
        list1 = []
        
        while (head != None):
            list1.append(head.val)
            head = head.next
        
        n= len(list1) - 1
        for i in list1:
            if i == list1[n]:                
                if n == len(list1)//2:
                    return True
                n -=1
            else:
                return False

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

# Test Cases
#head1 = [1,2,2,1]

node = Solution()
node.insert(1)
node.insert(2)
node.insert(2)
node.insert(1)
node.print()

obj = Solution()
print(obj.isPalindrome(node.head))

