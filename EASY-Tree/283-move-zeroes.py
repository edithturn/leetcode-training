# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

def moveZeroesBruteForce(nums):
    """
    First Approach Brute Force: For iterations:
    - To know the amount of zeros that we have
    - second: to add into a list al the non zeros number
    - four: Add into the list the amoung of zeroes that we already know
    - five: change the values of the originas list with our final list
    ||======= Big O ======= ||
    * Time complexity : O(n) 
    * Space complexity: O(n)
    """
    count = 0
    llist = []
    for n in nums:
        if n == 0:
            count += 1
    for i in range(len(nums)):
        if nums[i] != 0:
            llist.append(nums[i])
    
    while count > 0:
        llist.append(0)
        count -= 1
    
    for i in range(len(nums)): 
        nums[i] = llist[i]
    
    return nums

def moveZeroesTwopointers(nums):
        """
        Two Pointers aproach, using two pointers to iterate the list and get the nonzero numbers, then save it in the same list at the front of it.
        My second iteration will add the amount of zeros to complete the amoung of elemnents in our list (these will add at the end of the list)
        ||======= Big O ======= ||
        * Time complexity : O(n) 
        * Space complexity: O(1)
        """
        nonzero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1
        
        for i in range(nonzero, len(nums)):
            nums[i] = 0     

        return nums

nums1 = [0,1,0,3,12]
nums2 = [0]
print(moveZeroesBruteForce(nums1))
print(moveZeroesBruteForce(nums2))
print(moveZeroesTwopointers(nums1))
print(moveZeroesTwopointers(nums2))