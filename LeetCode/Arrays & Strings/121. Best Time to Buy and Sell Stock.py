# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Difficulty: Easy


# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        minBuy = 10**4
        maxProfit = 0

        for i in range(len(prices)):
            price = prices[i]

            if price < minBuy:
                minBuy = price
            
            else:
                profit = price - minBuy

                maxProfit = max(profit, maxProfit)

        return maxProfit
            
    

test = Solution()
print(test.maxProfit([7, 1, 5, 3, 6, 4]))


# Runtime: O(n)
