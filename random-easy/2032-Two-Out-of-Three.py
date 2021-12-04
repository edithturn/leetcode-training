def twoOutOfThree(nums1, nums2, nums3):
    
    together  = []
    final = {}
            
    together.extend(list(set(nums1)))
    together.extend(list(set(nums2)))
    together.extend(list(set(nums3)))
    
    
    for num in together:
        if num in final:
            final[num] += 1
        else:
            final[num] = 1
    
    together = []
    
    for key, value in final.items():
        if value > 1:
            together.append(key) 
            
    return together
    

print(twoOutOfThree([1,1,3,2],[2,3],[3]))   # [3,2]
print(twoOutOfThree([3,1],[2,3],[1,2]))     #  [2,3,1]
print(twoOutOfThree([1,2,2],[4,3,3],[5]))   # []