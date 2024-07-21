# class Solution(object):
#     def maxArea(self, height):
#         res = 0
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 l = min(height[i], height[j])
#                 w = j - i
#                 area = l * w
#                 res = max(area, res)

#         return res

class Solution(object):
    def maxArea(self, height):
        res = 0
        i = 0
        j = len(height) - 1

        while (i < j):
            w = j - i
            l = min(height[i], height[j])
            area = l * w
            res = max(area, res)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return res
    

test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))
print(test.maxArea([2,3,4,5,18,17,6]))

