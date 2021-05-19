# Write a method `combinations` that takes in a list of unique elements, and returns a 2D list representing all possible combinations of 2 elements of the list.

# combinations(["Blue", "Red", "Purple"]) # => [ [ "a", "b" ], [ "a", "c" ], [ "b", "c" ] ]

# combinations(["", 1, 2, 3]) # => [ [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ] ]



def combinations(list1, list2):
    
    _str = ""
    _list =[]
    
    for i in list1:
        _tmp_list = []
        for j in list2:
            if j != i:
                _str = i + j
                _tmp_list.append(_str)
        _list.append(_tmp_list)
    return _list    


   
list1 =  ['A', 'B', 'C', 'D', 'F']
list2 =  ['A','B', 'C', 'D']
print(combinations(list1, list2))


# What I learned:
    # Appliying a while into a for
    # Add a list into another list, clean it before append into final list
    # To iterate the same list two time and with a count increasing inone to track the second iteration