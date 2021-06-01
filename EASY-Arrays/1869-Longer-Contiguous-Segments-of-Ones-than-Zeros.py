# Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

# For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
# Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

# Exampel01
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.

# Exampel02
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.

# Exampel03
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.

def checkZeroOnes(s):
    """
    First Approach Brute Force: One iteration, and check longest segment of ones and zeros, reset the values each tiem that is not continue.
    Save the lingest contiguous segment and compare them after the loop.
    ||======= Big O ======= ||
    * Time complexity : O(n) 
    * Space complexity: O(1)
    """
    mayor_1 = 0
    mayor_0 = 0
    tmp_0 = 0
    tmp_1 = 0
    
    for i in s:
        if i == '1':
            tmp_1 += 1
            if tmp_1 > mayor_1:
                mayor_1 = tmp_1
            tmp_0 = 0
        elif i == '0':
            tmp_0 += 1
            if tmp_0 > mayor_0:
                mayor_0 = tmp_0
            tmp_1 = 0
            
    if mayor_1 > mayor_0:
        return True
        
    return False


# Test Cases
s1 = "1101"
s2 = "111000"
s3 = "110100010"
print(checkZeroOnes(s1))
print(checkZeroOnes(s2))
print(checkZeroOnes(s3))
