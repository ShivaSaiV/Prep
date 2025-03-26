class Solution:
    def maxProfit(self, prices):
        if prices is None:
            return 0

        maxProfit = 0
        left = 0

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                maxProfit = max(maxProfit, currProfit)
            else:
                left = right
        
        return maxProfit

            
            
