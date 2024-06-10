class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        n = len(candies)
        result = []
        max = 0
        for i in range(n):
            if candies[i] > max:
                max = candies[i]
        for i in range(n):
            if (candies[i] + extraCandies) >= max:
                result.append(True)
            else:
                result.append(False)
        return result
        