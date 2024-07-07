class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        res = numBottles

        while (numBottles >= numExchange):
            res += int(numBottles / numExchange)
            left = numBottles % numExchange
            numBottles = int(numBottles / numExchange) + left

        return res

    

test = Solution()
print(test.numWaterBottles(9, 3))
print(test.numWaterBottles(15, 4))