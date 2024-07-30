# https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        
test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
print(test.twoSum([3, 2, 3], 6))

# Runtime = O(n^2)

# Follow-up: Try to reduce runtime
class Solution2(object):
    def twoSum(self, nums, target):
        myDict = {}
        for i in range(len(nums)):
            myDict[nums[i]] = i

        print(myDict)

        for i in range(len(nums)):
            other = target - nums[i]
            if other in myDict:
                if myDict[other] != i:
                    return [i, myDict[other]]
             

test = Solution2()
print(test.twoSum([2, 7, 11, 15], 9))
print(test.twoSum([3, 2, 3], 6))