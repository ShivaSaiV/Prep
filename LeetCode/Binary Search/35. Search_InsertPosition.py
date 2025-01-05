# https://leetcode.com/problems/search-insert-position/
# Difficulty: easy

'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
Algorithm in O(log n) runtime complexity
'''

class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        if target > nums[-1]:
            return n

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m 
            
            if nums[m] > target:
                r = m - 1
            
            else:
                l = m + 1
        
        return l + 1

