def maximumWealth(accounts):
    """
    First Approach Brute Force: Using two loops, one to iterate the first list and other to iterate the sub list.
    In the secodn loop I am adding the values of all the sub list to get the total wealth per person.
    then I am getting the max wealth.

    ||======= Big O ======= ||
    - Time complexity : O(nk) where n is the elemets in the list and k is the elements in the sub list
    - Space complexity: O(1)
    """
    wealth = 0
    
    for i in range(len(accounts)):
        t_sum = 0
        for j in range(len(accounts[i])):
            t_sum += accounts[i][j]
        
        if t_sum > wealth:
            wealth = t_sum
    return wealth
                       


# Test Cases

accounts1 = [[1,2,3],[3,2,1]]
accounts2 = [[1,5],[7,3],[3,5]]
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]


print(maximumWealth(accounts1))
print(maximumWealth(accounts2))
print(maximumWealth(accounts3))
