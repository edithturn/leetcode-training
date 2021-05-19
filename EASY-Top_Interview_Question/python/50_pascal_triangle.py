
"""
This funciton will calculate the values of each row in the result of the Pascal's trieangule.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1  
"""
def generate(numRows):
    final_list = []

    # Creatign the list fina_list which will have the rows that we need to complete the Pascal's Trieangule
    for i in range(1, numRows + 1):
        # Initializing all the elements in the list  with zero 
        final_list.append([0]*i)

    # Adding 1 at the beggining and at the end of the list (each row)
    for value in final_list:
        value[0] =  1
        value[-1] = 1

    # Completing the empty values in the row, with the sum of both numbers of the previous list. We need to iterate the final_list and the sub list indise
    for i in range(len(final_list)):
        for j in range(len(final_list[i])):
            if final_list[i][j] ==0:
                final_list[i][j] = final_list[i-1][j] + final_list[i-1][j-1]
                
    return final_list

numRows = 5
print(generate(numRows))