# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# Difficulty: Medium

'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

# BFS
# Set A: for atlantic ocean
# Set P: for pacifici ocean
from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        pQ = deque()
        p_seen = set()

        aQ = deque()
        a_seen = set()

        rows, cols = len(heights), len(heights[0])
        
        # For pacific 
        for j in range(cols):
            pQ.append((0, j)) # Adding top wall, including top corner
            p_seen.add((0, j))
        
        for i in range(1, rows):
            pQ.append((i, 0)) # Adding left wall, excluding top corner
            p_seen.add((i, 0)) 
        

        # For atlantic
        for i in range(rows):
            aQ.append((i, cols-1)) # right wall, incliding right corner
            a_seen.add((i, cols-1))
        
        for j in range(cols-1):
            aQ.append((rows - 1, j)) # bottom row, excluding right corner
            a_seen.add((rows - 1, j))

        
        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i, j))
                for i_nei, j_nei in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i+i_nei, j + j_nei
                    if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
        
            return coords
        
        p_coords = get_coords(pQ, p_seen)
        a_coords = get_coords(aQ, a_seen)

        return list(p_coords.intersection(a_coords))


        