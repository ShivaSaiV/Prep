class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        prefix = [1] * n
        prefix[0] = 1
        suffix = [1] * n
        suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer
                