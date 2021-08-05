
def romanToInt(s):
    """
    Brute Force: Iterate the string in reverse, and chck if current values is grather than next one, so add to the total sum, on the contrary substract the current value
    ||======= Big O ======= ||
    Time complexity : O(n)
    Space complexity: O(1)
    """
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    # MCMXCIV
    total = 0
    aux = 0
    for i in s[::-1]:
        if roman[i] >= aux:
            total += roman[i]
        else:
            total -= roman[i]            
        aux =roman[i]                
    return total

# Test Cases

s = "III" # 3
p = "IV" # 4
k = "IX" # 9
f = "LVIII" # 58 Explanation: L = 50, V= 5, III = 3.
l = "MCMXCIV" # 1994 Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

print(romanToInt(s))
print(romanToInt(p))
print(romanToInt(k))
print(romanToInt(f))
print(romanToInt(l))