# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

def shuffle(nums, n):
    """
    First Approach Brute Force: Create an empty list where I will storage
    the sum of each element iterated in the loop. The loop will iterate the half of the list (x elements), 
    and adding how next element the next position the list of y elemets.
    ||======= Big O ======= ||
    - Time complexity : O(n) where "n" is the number of elements in the mums list.
    - Space complexity: O(1) because the output array is not take into consideration    
    """
    nlist = []
    
    for i in range(0, len(nums)//2):
        nlist.append(nums[i])
        nlist.append(nums[i + n])
    return nlist
    
    