"""
First approach, cheking if the element is in the list numer2, 
if it is then add it into a new list and then remove from the list number02 to avoud duplications
"""

def intersect(nums1, nums2):
    res = []
    for n in nums1:
        if n in nums2:
            res.append(n)
            nums2.pop(nums2.index(n))
    return res

        



nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

print(intersect(nums1,nums2))
print(intersect(nums3,nums4))