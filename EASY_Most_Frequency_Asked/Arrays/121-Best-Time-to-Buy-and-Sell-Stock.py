# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# # Example 1:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def maxProfitI(prices):
    """
    First Approach Brute Force: Creted two loops, the first one to evaluate two element in the list, choose the one that is lower to 
    to the best day to buy, and compare it with the next element in the list, saving the subtraction in a list.
    The second loop will the the maximum number in the list and it will be the max profit.

    ||======= Big O ======= ||
    - Time complexity : O(n) where "n" is the number of elements in the mums list.
    - Space complexity: O(n - 1) I have a list and it will be the result of the substracion of the list
    """
    min_cost_buy = prices[0]
    profits = []
    
    for i in range(len(prices) - 1):         
        profits.append(prices[i + 1] - min_cost_buy)
        if prices[i + 1]  < min_cost_buy:
            min_cost_buy = prices[i + 1]
    max_price_sell = 0        
    for i in profits:
        if i > max_price_sell and i > 0:
            max_price_sell = i
    return max_price_sell


def maxProfitII(prices):
    """
    Second Approach, optimization: Creted one loop to evaluate two element in the list, choose the one that is lower to 
    to the best day to buy, and compare it with the next element in the list, saving the subtraction in a list.
    Also calculating the max value of a profit in each loop.

    ||======= Big O ======= ||
    - Time complexity : O(n) where "n" is the number of elements in the mums list.
    - Space complexity: O(1) I have just tow variables
    """
    min_cost_buy = prices[0]
    max_price_sell = 0

    for i in range(len(prices) - 1):         
        if ((prices[i + 1] - min_cost_buy) > max_price_sell):
            max_price_sell = prices[i + 1] - min_cost_buy
        if prices[i + 1]  < min_cost_buy:
            min_cost_buy = prices[i + 1]
             
        
    return max_price_sell

# Test Cases

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(maxProfitI(prices1))
print(maxProfitI(prices2))

print(maxProfitII(prices1))
print(maxProfitII(prices2))