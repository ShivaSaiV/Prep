# https://leetcode.com/problems/combinations/description/
# Difficulty: Medium

'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
'''

class Solution(object):
    def combine(self, n, k):
        res = []

        sol = []

        def backtrack(start):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for i in range(start, n + 1):
                sol.append(i)
                backtrack(i + 1)
                sol.pop()
            
        backtrack(1)
        return res
