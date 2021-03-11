# Write a method `combinations` that takes in a list of unique elements, and returns a 2D list representing all possible combinations of 2 elements of the list.

# combinations(["a", "b", "c"]) # => [ [ "a", "0" ], [ "a", "c" ], [ "b", "c" ] ]

# combinations([0, 1, 2, 3]) # => [ [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ] ]

def combinations_3(list1, list2):
    tmp_list = []
    final_list = []
    for el1 in list1:
           for el2 in list2:
            tmp_list = []
            if el2 != el1:
                tmp_list.append(el1)
                tmp_list.append(el2)
                final_list.append(tmp_list)
    return final_list


list1 =  ['a', 'e', 'i']
list2 =  ['a', 'h', 'e' ,'v', 'y', 'x']
print(combinations_3(list1, list2))

# What I learned:
    # Appliying a while into a for
    # Add a list into another list, clean it before append into final list
    # To iterate the same list two time and with a count increasing inone to track the second iteration