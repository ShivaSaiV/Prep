from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while (start < end):
            if (height[start] > height[end]):
                area = height[end] * (end-start)
            else:
                area = height[start] * (end-start)
            if (area > max_area):
                max_area = area
            if (height[start] < height[end]):
                start += 1
            else:
                end -= 1
        return max_area
