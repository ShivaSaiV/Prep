# https://leetcode.com/problems/summary-ranges/description/ 
# Difficulty: easy

# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, 
# and there is no integer x such that x is in one of the ranges but not in nums.

# Range has only continuous numbers

class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        starts = []
        ends = []
        start = nums[0]
        starts.append(start)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            if nums[i] - nums[i-1] != 1:
                start = nums[i]
            end = nums[i-1]
            starts.append(start)
            ends.append(end)
        ends.append(nums[-1])
        print(ends)

        res = []

        for i in range(len(ends)):
            if starts[i] != ends[i]:
                res.append(str(starts[i]) + "->" + str(ends[i]))
            else:
                res.append(str(starts[i]))
        return res
            


test = Solution()
print(test.summaryRanges([0,1,2,4,5,7]))
print(test.summaryRanges([0,2,3,4,6,8,9]))
