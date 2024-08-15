# https://leetcode.com/problems/product-of-array-except-self/description/
# Difficulty: medium

# Given an integer array nums, return an array answer such that answer[i] is equal 
# to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Hard part was crating suffix array

class Solution(object):
    def productExceptSelf(self, nums):
        prefixProduct = []
        prefix = 1
        prefixProduct.append(prefix)
        
        for i in range(1, len(nums)):
            prefix = prefix * nums[i - 1]
            prefixProduct.append(prefix)

        suffixProduct = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1 ):
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1]

        print(suffixProduct)
        res = []

        for i in range(len(suffixProduct)):
            res.append(suffixProduct[i] * prefixProduct[i])

        return res

    
test = Solution()
print(test.productExceptSelf([1, 2, 3, 4]))