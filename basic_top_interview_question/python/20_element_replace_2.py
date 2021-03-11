# Element Replace
# Write a method element_replace that takes in a list and a dictionary. The method should return a new list where elements of the original list are replaced with their corresponding values in the dictionary.

# list1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
# dict1 = {"Serena Williams": "tennis", "LeBron James": "basketball"}

# element_replace(list1, dict1) # => ["basketball", "Lionel Messi", "tennis"]

# list2 = ["dog", "cat", "mouse"]
# dict2 = {"dog": "bark", "cat": "meow", "duck": "quack"}

# element_replace(list2, dict2) # => ["bark", "meow", "mouse"]


def element_replace(_list, _dic):
    new_list = []
    for item in _list:
        if item in _dic:
           new_list.append(_dic[item])
        else:
            new_list.append(item)
    return new_list
list1 = ["LeBron James", "Lionel Messi", "Serena Williams"]
dict1 = {"Serena Williams": "tennis", "LeBron James": "basketball"}


list2 = ["dog", "cat", "mouse"]
dict2 = {"dog": "bark", "cat": "meow", "duck": "quack"}

print(element_replace(list1, dict1))
print(element_replace(list2, dict2))