# https://leetcode.com/problems/combination-sum/description/
# Difficulty: Medium

'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        n = len(candidates)

        res = []
        sol = []

        def backtrack(i, currSum):
            currSum = sum(sol)
            if currSum == target:
                res.append(sol[:])
                return
            elif currSum < target:
                for j in range(i, len(candidates)):
                    sol.append(candidates[j])
                    currSum = sum(sol)
                    backtrack(j, currSum + candidates[j])
                    sol.pop()
            else:
                return

        backtrack(0, 0)
        return res 


test = Solution()
print(test.combinationSum([2, 3, 6, 7], 7))