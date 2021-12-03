def uniqueOccurrences(arr):
    """
    Using set, to get unique values in an array

    BigO:
    Tim: O(n)
    Space: O(1)
    """
        
    repeat = []    
    uniques = set(arr)
    
    for item in uniques:
        repeat.append(arr.count(item))
    
    return len(repeat) == len(set(repeat))
    
    

print(uniqueOccurrences([1,2,2,1,1,3])) # true
print(uniqueOccurrences([1,2])) # false
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true