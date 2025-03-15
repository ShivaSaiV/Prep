# https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Difficulty: Medium

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
'''

class Solution(object):
    def longestOnes(self, nums, k):
        maxsize = 0
        num_zeros = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            w = r - l + 1
            maxsize = max(maxsize, w)


        return maxsize
