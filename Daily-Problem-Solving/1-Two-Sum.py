def twoSum(nums, target):
    """
    using HashTable to identify if the complent is already in it
    """
    result = {}
    complement = 0
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in result:
            result[num] = i
        else:
            return [result[complement], i]
    return []


# Test Cases
nums1 = [2,5,5,11]
target1 = 10

nums2 = [2,7,11,15]
target2 = 9

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))