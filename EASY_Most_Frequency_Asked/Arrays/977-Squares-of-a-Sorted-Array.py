# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


def sortedSquares(nums):     
    """
    First Approach: Two pointers:  We are using two pointer, to iterate the number for the beginning and for the end at the same time.
    after compare and choose the higher number, we add it to the end of the new array (we add the square of the number)
    ||======= Big O ======= ||
    - Time complexity : O(n) : n is the len of the array.
    - Space complexity: O(n) , where n is the len of the array, we are creating an array to store the square of each element in the array
    """
    
    left = 0
    right = len(nums) - 1
    result = [0]*len(nums)
    n = len(nums) - 1
    
    while n >= 0:            
        if nums[left] < 0:
            nums[left] = nums[left]*(-1)
        if nums[right] < 0:
            nums[right] = nums[right]*(-1)
        
        if nums[left] < nums[right]:
            max_number = nums[right]
            right -= 1
        else:
            max_number = nums[left]
            left  += 1
        result[n] = max_number * max_number
        n -= 1
    
    return result
                

# Test Cases        

nums1 = [-4,-1,0,3,10]
nums2 = [-7,-3,2,3,11]

print(sortedSquares(nums1))
print(sortedSquares(nums2))