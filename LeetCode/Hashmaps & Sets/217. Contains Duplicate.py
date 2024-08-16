# https://leetcode.com/problems/contains-duplicate/description/
# Difficulty: Easy

# Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        myDict = {}

        for i in nums:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        
        for val in myDict.values():
            if val > 1:
                return True

        return False

test = Solution()
print(test.containsDuplicate([1, 2, 3, 4]))

        