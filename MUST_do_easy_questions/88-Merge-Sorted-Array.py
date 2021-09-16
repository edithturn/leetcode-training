
def merge(nums1, m, nums2, n):
    """
    Using tow stacks: Using three pointers, compare values between nums1 and nums2, if one of them is grather than the other, insert it on the end of nums1.
    ||======= Big O ======= || 
    Time complexity : O(n)
    Space complexity: O(1)
    """
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1] 
            nums1[m - 1]  = nums2[n - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]