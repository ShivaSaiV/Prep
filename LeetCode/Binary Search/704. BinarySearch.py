# https://leetcode.com/problems/binary-search/
# Difficulty: easy

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
Algorithm should be in O(log n) runtime complexity
'''

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m 
            
            if nums[m] > target:
                r = m - 1
            
            else:
                l = m + 1
        
        return -1