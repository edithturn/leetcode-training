
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


# Example 1:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# memoization: Cache values

"""
==> Dinamic Programming and Fibonacci

To solve this problem we have to cached the value, then return it if n already exit in a cache
Fibonacci:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711...
Using Dinamic Programming to solve this problem, recursion work fine but this is good with time complexity. 
Using DP and Fibonacci to solve this problem:
Example:
f(0) and f(1) = 1
f(2) = f(2 - 1) + f(2 - 2)     = 1
f(3) = 3 = f(3 - 1) + f(3 - 2) = 3
f(4) = 5 = f(4 - 1) + f(4 - 2) = 5
Time Comexity: Time: O(N)  Space: O(1)
"""
def climbStairs(n):
    # Creating a list with n + 1 of zise with zero as a value, example: n = 5 : [0, 0, 0, 0, 0, 0]
    ways_climb = [0]*(n+1)
    # Fibonn
    ways_climb[0] = 1
    ways_climb[1] = 1
    # Calculating the fibonacci of each value until n
    for step in range(2, n + 1):
        # Appliying Fibonacci, if the value exist in the list we will use use it and don't calculate it again
        ways_climb[step] = ways_climb[step - 1] + ways_climb[step - 2]
    # Returning the ways how we can climb the starts with one step or 2 steps
    return ways_climb[n]
"""
Testing
"""
n = 5
m = 4
print(f"We can climb {n} in {climbStairs(n)} steps")
print(f"We can climb {n} in {climbStairs(m)} steps")