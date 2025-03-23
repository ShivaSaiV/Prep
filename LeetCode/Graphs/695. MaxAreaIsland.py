# https://leetcode.com/problems/max-area-of-island/description/
# Difficulty: Medium

'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        if grid is None:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0
                currArea = 1 + dfs(r, c + 1) + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1)
                return currArea

        
        num_islands = 0
        # Iterate through grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currArea = dfs(r, c)
                    maxArea = max(currArea, maxArea)
                    num_islands += 1
        
        if num_islands == 0:
            return 0
        else:
            return maxArea
    

test = Solution()
print(test.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))