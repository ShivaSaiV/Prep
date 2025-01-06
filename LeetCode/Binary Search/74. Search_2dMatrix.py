# https://leetcode.com/problems/search-a-2d-matrix/description/
# Difficulty: medium

'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        i = 0
        print(rows)

        while (i < rows):
            l = 0
            r = len(matrix[0]) - 1
            print(r)

            while l <= r:
                mid = l + ((r - l) // 2)
                
                if matrix[i][mid] == target:
                    return True
                
                if matrix[i][mid] > target:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            i += 1
        
        return False

test = Solution()
# print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(test.searchMatrix([[1]], 0))