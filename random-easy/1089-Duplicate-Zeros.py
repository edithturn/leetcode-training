def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    # arr = [1,0,2,3,0,4,5,0]
    i = 0
    while i < len(arr)-1:            
        if arr[i] == 0:           
            arr.pop(-1)
            arr.insert(i, arr[i])  
            i += 1                 
        i += 1                     
    return arr
    
print(duplicateZeros([1,0,2,3,0,4,5,0]))
print(duplicateZeros([1,2,3]))
print(duplicateZeros([0,0,0,0,0,0,0]))