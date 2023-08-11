# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        if len(prices) == 0:
            return 0
        
        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices [left]

            if prices[right] > prices[left]:
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
    

    def maxProfit2(self, prices):
        max_profit = 0
        if len(prices) == 0:
            return 0
        first = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - first)
            first = min(first, prices[i])

        if max_profit > 0:
            return max_profit
        else:
            return 0