class Solution(object):

    # # Can improve time complexity
    # def minOperations(self, nums):
    #     count = 0
    #     for i in range(len(nums) - 1):
    #         if nums[i + 1] <= nums[i]:
    #             while nums[i + 1] <= nums[i]:
    #                 nums[i + 1] += 1
    #                 count += 1
    #     return count

    def minOperations(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i] + 1:
                curr_count = 0
                curr_count += nums[i] - nums[i + 1] + 1
                count += nums[i] - nums[i + 1] + 1
                nums[i + 1] += curr_count

        return count
    
test = Solution()
print(test.minOperations([1, 1, 1]))
print(test.minOperations([8]))
print(test.minOperations([1,5,2,4,1]))