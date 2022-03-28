def sortColorsI(nums):
    """
    Force Brute: Compare the first element with the rest of element and swap them if this is grather than others.

    Big O
    -----
    * Time:  O(n²): The inner loop is executed i times, for each value of i. The outer loop is executed n times.
    * Space: O(1), no additional memory set
    """
    le = len(nums)
            
    for i in range(le):
        r  = le - 1
        while  r >= i:
            if nums[i] > nums[r]:
                nums[i], nums[r] = nums[r], nums[i]
            r -= 1
    return nums
    
def sortColorsII(nums):
    """
    Three Pointers: Since there are just three colors we can set an if for each one, locating the higher number at the end of the array.

    Big O
    -----
    * Time:  O(n): Every element will be processed once.
    * Space: O(1), no additional memory set
    """
    left, right, i = 0, len(nums) - 1 , 0
    
    while  i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i +=1
    return nums
                    
# Test cases
print(sortColorsI([2,0,2,1,1,0])) # OutPut: [0, 0, 1, 1, 2, 2]
#print(sortColorsI([2,0,1]))

print(sortColorsII([2,0,2,1,1,0])) # OutPut: [0, 0, 1, 1, 2, 2]
#print(sortColorsII([2,0,1]))


   
