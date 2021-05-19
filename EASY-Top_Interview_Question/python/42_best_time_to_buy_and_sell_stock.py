def maxProfit(prices):
    maxprofit, res  = 0, 0
    for i in range(1, len(prices)):
        maxprofit += prices[i] - prices[i - 1]
        res = max(res, maxprofit)
        if maxprofit < 0:
            maxprofit = 0
    return res


prices0  = [4,-5,4,-3,4,4,-4,4,5]
prices  = [7,1,5,3,6,4]
prices1 = [7,6,4,3,1]
print(maxProfit(prices0))
print("  ")
print(maxProfit(prices))
print("  ")
print(maxProfit(prices1))


#[1, 3, 4, 5, 6, 7]
#{7: 0, 1: 1, 5: 2, 3: 3, 6: 4, 4: 5}