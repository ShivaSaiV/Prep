class Solution:
    def maxArea(self, heights):
        if heights is None:
            return 0
        
        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] <= heights[right]:
                area = (right - left) * heights[left]
            else:
                area = (right - left) * heights[right]
            
            res = max(area, res)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return res

