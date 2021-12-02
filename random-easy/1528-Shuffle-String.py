
def restoreString( s, indices):
    """
    Using dictionary

    Big O:
    Time: O(n), where n is the numbeer of elements in the array
    Space: O(n), where n is the dictionary with elements of indices and s
    """
    counter = 0
    result = ""
    dic = {}
    
    for i in indices:
        dic[i] = s[counter]    
        counter += 1
        
    for i in range(len(indices)):
        result = result + dic[i]
    return result

# Test Cases


print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))  #leetcode
print(restoreString("abc", indices = [0,1,2]))      #abc
print(restoreString("aiohn", indices = [3,1,4,2,0])) #nihao
print(restoreString("aaiougrt", indices = [4,0,2,6,7,3,1,5])) #arigatou
