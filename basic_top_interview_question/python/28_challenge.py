# Element Replace
# Write a method element_replace that takes in a list and a dictionary. The method should return a new list where elements of the original list are replaced with their corresponding values in the dictionary.

# list1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
# dict1 = {"Serena Williams": "tennis", "LeBron James": "basketball"}

# element_replace(list1, dict1) # => ["basketball", "Lionel Messi", "tennis"]


# list2 = ["dog", "cat", "mouse"]
# dict2 = {"dog": "bark", "cat": "meow", "duck": "quack"}

# element_replace(list2, dict2) # => ["bark", "meow", "mouse"]

# With enumerate
def element_replace(list1, dic1):
    mylist  = []
    for index, val in enumerate(list1):
       if val in dic1:
           mylist.append(dic1[val])
       else:
           mylist.append(list1[index])
    return mylist


#With Index
def element_replace1(list1, dic1):   
    mylist1 = []
    for i in range(len(list1)):
        if list1[i] in dic1:
            mylist1.append(dic1[list1[i]])
        else:
            mylist1.append(list1[i])
    return mylist1

list2 = ["dog", "cat", "mouse"]
dict2 = {"dog": "bark", "cat": "meow", "duck": "quack"}

print(element_replace(list2, dict2)) # => ["bark", "meow", "mouse"]
print(element_replace1(list2, dict2)) # => ["bark", "meow", "mouse"]