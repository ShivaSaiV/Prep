# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Difficulty: easy

# Given an integer array nums sorted in non-decreasing order,
#  return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        squared = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            squared[i] = nums[i] * nums[i]
        
        while (left <= right):
            toAdd = max(squared[left], squared[right])
            if squared[right] > squared[left]:
                toAdd = squared[right]
                res.append(toAdd)
                right -= 1
            else:
                toAdd = squared[left]
                res.append(toAdd)
                left += 1

        return res[::-1]

test = Solution()
print(test.sortedSquares([-4, -1, 0, 3, 10]))
