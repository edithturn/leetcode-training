# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

def addStrings(num1, num2):
    """
    First Approach Force Brute Math

    ||======= Big O ======= ||
    - Time complexity : O(max(n1, n2)) where n1 and n2 is the size of n1 and n2, respectively
    - Space complexity: O(max(n1, n2))
​	
 ))
    """
    tsum = []
    carry = 0
    
    len1 = len(num1) - 1
    len2 = len(num2) - 1
    
    while len1 >= 0 or len2 >= 0:
        if len1 >= 0:
            n1 = ord(num1[len1]) - ord('0')
        else:
            n1 = 0
    
        if len2 >= 0:
            n2 = ord(num2[len2]) - ord('0')
        else:
            n2 = 0
        
        tmp_sum = (n1 + n2 + carry)%10
        carry = (n1 + n2 + carry)//10
        len1 -= 1
        len2 -= 1            
        tsum.append(tmp_sum)
    
    if carry:
        tsum.append(carry)
    res = ''.join((str(n) for n in tsum[::-1]))
    
    return res
            
# Test Cases

num1 = "0"
num2 = "0"

num3 = "456"
num4 = "77"

num5 = "11"
num6 = "123"


print(addStrings(num1, num2))
print(addStrings(num3, num4))
print(addStrings(num5, num6))