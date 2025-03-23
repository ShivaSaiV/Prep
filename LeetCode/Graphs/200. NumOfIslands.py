# https://leetcode.com/problems/number-of-islands/description/
# Difficulty: Medium

'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
# DFS with recursion
class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i, j + 1) # Going right
                dfs(i + 1, j) # Going down
                dfs(i, j - 1) # Going left
                dfs(i - 1, j) # Going up


        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands




# BFS with queue
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()
        num_islands = 0

        # bfs
        def bfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if ((r + dr) in range(rows) and (c + dc) in range(cols) and grid[r + dr][c + dc] == "1" and (r + dr, c + dc) not in seen):
                        q.append((r + dr, c + dc))
                        seen.add((r + dr, c + dc))


        # iterate through the grid and find 1s
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands