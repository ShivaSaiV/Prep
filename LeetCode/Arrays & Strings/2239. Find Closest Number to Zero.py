# https://leetcode.com/problems/find-closest-number-to-zero/description/
# Difficulty: Easy

import math
class Solution(object):
    def findClosestNumber(self, nums):
        minDist = 10**5
        maxVal = 10**5
        pos = False
        for i in nums:
            if i > 0:
                pos = True
            dist = abs(i)
            val = i
            if minDist < dist:
                continue
            if minDist > dist:
                minDist = dist
                maxVal = val
            if minDist == dist:
                maxVal = max(maxVal, val)
        if pos == False:
            return nums[0]
        return maxVal


test = Solution()
print(test.findClosestNumber([-4,-2,1,4,8]))
print(test.findClosestNumber([2,-1,1]))
print(test.findClosestNumber([-100000,-100000]))

# Time complexity: O(n)