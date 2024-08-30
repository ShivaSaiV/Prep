# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Difficulty: Easy

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        

test = Solution()
print(test.twoSum([2,7,11,15], 9))