
def rotate(nums, k):
    """
    Reversing array: Reverse the array, then reverse the first "k" elements, finally reverse the elements remaining since "k" onwards
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

    return nums
    
    
def reverse(nums, start, end):
    while(start < end):
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        start += 1
        end -= 1

# Test Cases
nums1 = [1,2,3,4,5,6,7]
k1 = 3

nums2 = [-1,-100,3,99]
k2 = 2

print(rotate(nums1, k1))
print(rotate(nums2, k2))