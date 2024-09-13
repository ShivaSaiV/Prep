# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        res = 0

        while start < end:
            length = min(height[start], height[end])
            width = end - start
            area = length * width
            if res < area:
                res = area

            if height[start] < height[end]:
                start += 1
            elif height[end] < height[start]:
                end -= 1
            else:
                start += 1
                end -= 1

        return res
    
test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))

