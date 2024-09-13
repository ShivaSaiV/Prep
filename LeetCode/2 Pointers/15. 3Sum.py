# https://leetcode.com/problems/3sum/description/
# Difficulty: medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                if nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
        return res
    

test = Solution()
print(test.threeSum([-1,0,1,2,-1,-4]))