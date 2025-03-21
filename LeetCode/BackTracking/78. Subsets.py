# https://leetcode.com/problems/subsets/description/
# Difficulty: Medium

'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# Time: O(2^N)
# Space: O(N)

class Solution(object):
    def subsets(self, nums):
        n = len(nums)

        # Final result
        res = []

        # Each individual element in res
        sol = []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            # Undo the backtrack
            sol.pop()
        
        backtrack(0)
        return res

test = Solution()
print(test.subsets([1, 2, 3]))