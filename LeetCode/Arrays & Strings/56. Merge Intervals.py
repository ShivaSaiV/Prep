# https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of 
# the non-overlapping intervals that cover all the intervals in the input.

class Solution(object):
    def merge(self, intervals):
        res = []
        intervals.sort()

        if len(intervals) == 0:
            return [[]]
        if len(intervals) == 1:
            return intervals
        
        res.append(intervals[0])
        

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])

        return res
    


test = Solution()
print(test.merge([[1,4],[0,2],[3,5]]))
print(test.merge([[1,3],[2,6],[8,10],[15,18]]))
print(test.merge([[1, 4], [5, 6]]))