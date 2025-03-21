# https://leetcode.com/problems/permutations/description/
# Difficulty: Medium

'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

class Solution(object):
    def permute(self, nums):
        n = len(nums)

        res = []

        sol = []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
                

        backtrack()

        return res 