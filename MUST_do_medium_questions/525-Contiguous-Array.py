def findMaxLength(nums):
    """
    Using hashmap to save unique values. Starting the hash in -1 to get the lengh of ones and zeros
    Big O:
    Time Complexity: O(n), loop to traverse the nums
    Space Complexity: O(n), the worst case, if the hashmap turn into: [1,1,1,1,1,1] or [0,0,0,0,0,0]
    """
    _len = len(nums)
    hashMap = {0:-1}
    count = 0
    max_len = 0
            
    for index, value in enumerate(nums):
        if value == 0:
            count -= 1
        else:
            count += 1
    
        if count in hashMap:
            j = index-hashMap.get(count)
            max_len = max(max_len, j)
        else:
            hashMap[count] = index

    return max_len
    
print(findMaxLength([0,1,1,0,1,1,0,1])) # 4