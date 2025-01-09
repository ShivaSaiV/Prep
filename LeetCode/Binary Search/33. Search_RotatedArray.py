# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: medium

'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m 

            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

test = Solution()
print(test.search([1], target = 0))
print(test.search([4,5,6,7,0,1,2], target = 3))
print(test.search([4,5,6,7,0,1,2], target = 0))