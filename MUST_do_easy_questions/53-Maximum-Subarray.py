def maxSubArray(nums):
    current = nums[0]
    max_array = nums[0]

    for i in nums[1:]:
        current = max(i, current + i)
        max_array = max(current, max_array)
    return max_array


nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5,4,-1,7,8]


print(maxSubArray(nums1))
print(maxSubArray(nums2))
print(maxSubArray(nums3))