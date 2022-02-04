def intersection(nums1, nums2):
    p1 = 0
    p2 = 0
    res = set()
    nums1.sort()
    nums2.sort()
    while p1 < len(nums1) and p2 < len(nums2):        
        if nums1[p1] < nums2[p2]:
            p1 += 1
            continue
        if nums1[p1] > nums2[p2]:
            p2 += 1
            continue
        res.add(nums1[p1])
        p1 += 1
        p2 += 1
    return res


print(intersection([1,2,2,1],[2,2]))
print(intersection([4,9,5],[9,4,9,8,4]))
