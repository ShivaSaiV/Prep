# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Difficulty: Medium

'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):

        # Edge case1
        if max(nums) >= target:
            return 1

        # Edge case2
        if sum(nums) < target:
            return 0

        l = 0
        final_size = 10 ** 9

        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while (curr_sum >= target):
                w_size = r - l + 1
                final_size = min(w_size, final_size)
                curr_sum -= nums[l]
                l += 1

        return final_size

test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))
                

        