# https://leetcode.com/problems/maximum-average-subarray-i/description/
# Difficulty: easy

'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

'''

class Solution1(object):
    def findMaxAverage(self, nums, k):
        idx = 0
        res = -1.0 * 10**4

        if len(nums) == 1:
            return nums[0]

        if len(nums) == k:
            return float(sum(nums)) / k

        # loop over all elements O(n)
        while (idx <= len(nums) - k):
            curr_arr = nums[idx:idx+k]
            curr_sum = sum(curr_arr)
            curr_avg = float(curr_sum) / k
            res = float(max(curr_avg, res))
            idx += 1
        
        return res

# test = Solution()
# print(test.findMaxAverage([0, 1, 1, 3, 3], 4))
# print(test.findMaxAverage([1,12,-5,-6,50,3], 4))
# print(test.findMaxAverage([4,0,4,3,3], 5))


# Sliding Window
class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k
        res = float(-1 * 10**4)
        if len(nums) == 1:
            return nums[0]

        if len(nums) == k:
            return float(sum(nums)) / k


        curr_sum = float(sum(nums[left:k]))
        res = curr_sum / float(k)

        for _ in range(k, len(nums)):
            curr_sum -= nums[left]
            curr_sum += nums[right]
            avg = curr_sum / float(k)
            res = max(avg, res)

            left += 1
            right += 1

        return res

test = Solution()
# print(test.findMaxAverage([0, 1, 1, 3, 3], 4))
# print(test.findMaxAverage([1,12,-5,-6,50,3], 4))
print(test.findMaxAverage([9,7,3,5,6,2,0,8,1,9], 6))