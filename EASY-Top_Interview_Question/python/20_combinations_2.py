# Write a method `combinations` that takes in a list of unique elements, and returns a 2D list representing all possible combinations of 2 elements of the list.

# combinations(["a", "b", "c"]) # => [ [ "a", "b" ], [ "a", "c" ], [ "b", "c" ] ]

# combinations([0, 1, 2, 3]) # => [ [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ] ]

def combinations_2(my_list):
    tmp_list = []
    final_list = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            tmp_list = []
            tmp_list.append(my_list[i])
            tmp_list.append(my_list[j])
            final_list.append(tmp_list)
    return final_list

list1 =  ['a', 'b', 'c']
list2 =  [0, 1, 2, 3]
print(combinations_2(list1))
print(combinations_2(list2))

# What I learned:
    # Appliying a while into a for
    # Add a list into another list, clean it before append into final list
    # To iterate the same list two time and with a count increasing inone to track the second iteration