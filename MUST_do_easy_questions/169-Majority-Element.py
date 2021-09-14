
def majorityElement(nums):
    count = 0
    current = nums[0]
    
    for n in nums:
        if n == current:
            count += 1
        else:
            if count <= 0:
                current = n
                count = 1
            else:
                count -= 1
                
    return current


# Test
nums1 = [3,2,3]
nums2 = [2,2,1,1,1,2,2]

print(majorityElement(nums1))
print(majorityElement(nums2))