# https://leetcode.com/problems/majority-element/description/
# Difficulty: easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        target = len(nums) // 2

        myDict = {}

        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        for k, v in myDict.items():
            if v > target:
                return k

test = Solution()
print(test.majorityElement([2, 3, 3]))