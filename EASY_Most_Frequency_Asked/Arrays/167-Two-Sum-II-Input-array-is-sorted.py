# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2] 

# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.


def twoSum(numbers, target):
    """
    First Approach Two Pointers to add the numbers from the beginning and from the end to compare with the target.

    ||======= Big O ======= ||
    - Time complexity : O(n), iterating the list just one time
    - Space complexity: O(1) , we don't use extra espace
    """
    i = 0
    j = len(numbers) - 1
    res = []
    
    while i<j:
        left = numbers[i]
        right = numbers[j]
        
        if left + right == target:
            res.append(i + 1)
            res.append(j + 1)
            break
        elif left + right < target:
            i += 1
        else:
            j -= 1
    return res
            

# Test Cases

numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

numbers3 = [-1,0]
target3 = -1

print(twoSum(numbers1, target1))
print(twoSum(numbers2, target2))
print(twoSum(numbers3, target3))