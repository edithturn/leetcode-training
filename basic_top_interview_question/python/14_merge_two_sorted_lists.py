# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]

class Solution:
    def mergeTwoLists(self, l1, l2):
        new_list = []
        i = 0
        for lst1 in l1:
            if lst1 == l2[i]:
                new_list.append(lst1)
                new_list.append(lst1)
                i +=1
            else:
                new_list.append(lst1)
                new_list.append(l2[i])
                i +=1
        print(new_list)





l1 = [1, 2, 4]
l2 = [1, 3, 4, 5]

l3 = []
l4 = []

l5 = []
l6 = [0]

obj = Solution()
obj.mergeTwoLists(l1, l2)
obj.mergeTwoLists(l3, l4)
obj.mergeTwoLists(l5, l6)