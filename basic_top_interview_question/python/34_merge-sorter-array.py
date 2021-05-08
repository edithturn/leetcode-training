def merge(nums1, m , nums2, n):
    end = m 
    start = 0

    if m + n == 1:
        if m > n:
            return nums1
        else:
            return nums2

    while end < (len(nums1)):
        nums1[end] = nums2[start]
        end += 1
        start +=1
    nums1.sort()
    return nums1


nums1 = [1,2,3,0,0,0]
m1 = 3
nums2 = [2,5,6]
n2 = 3

nums3 = [1]
m3 = 1
nums4 = []
n4 = 0

nums5 = [1,2,0,0,0]
m5 = 2
nums6 = [3,5,7]
n6 = 3


nums7 = [0]
m7 = 0
nums8 = [1]
n8 = 1


print(merge(nums1, m1, nums2, n2))
print(merge(nums3, m3, nums4, n4))
print(merge(nums5, m5, nums6, n6))
print(merge(nums7, m7, nums8, n8))