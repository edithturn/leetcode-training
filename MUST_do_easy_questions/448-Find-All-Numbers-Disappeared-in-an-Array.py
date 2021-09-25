def findDisappearedNumbers(nums):
    """
    Reducing the firts list with set, no repitations and savign the elements that are not in range ( 1 -  n) in a new list. This is the answer.
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(n)
    """
    l = len(nums)
    nums = set(nums)
    a= []
    
    for i in range(1, l + 1):
        if i not in nums:
            a.append(i)
    return a

# Test Cases
nums1 = [4,3,2,7,8,2,3,1]
nums2 = [1,1]

print(findDisappearedNumbers(nums1)) # [5, 6]
print(findDisappearedNumbers(nums2)) # [2]