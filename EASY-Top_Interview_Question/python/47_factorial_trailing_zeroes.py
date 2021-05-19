"""
Calculating the factorial to get the result of this and use it to know how many zeros are at the end.
To calculate the amoung of zeros we are getting the remaint of the division by 10, so if this result is zero it means that is divisible and it has an zero at the end.
I will keep calculating the remain of the new result until there is not more. I am updatign the value of answer each time by a new vivision by 10.

++ Time Complexity ++
Time: O(log n)
"""
def trailingZeroes(n):
    answer = factorial(n)
    count = 0
    if answer < 10:
        return 0
    else:
        while answer % 10 == 0:
            answer = answer//10
            if answer < 10:
                break
            count += 1
    return count

def factorial(n):
    fact = 1
    for  i in range(1, n + 1):
        fact =  fact*i
    return fact

n = 3
n1 = 5
n2 = 30
print(trailingZeroes(n))
print(trailingZeroes(n1))
print(trailingZeroes(n2))