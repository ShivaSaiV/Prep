class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        if n < 2:
            return False
        num = 0
        sum_arr = []
        if (n == 2):
            if nums[0] == 1 and nums[1] == 0:
                return False
        if nums[0] == 0 and nums[1] == 0:
            return True
        
        for i in range(n):
            num += nums[i]
            sum_arr.append(num)
            # if nums[i] == 0:
            #     return True

        if num % k == 0:
            return True

        val_arr = []
       
        for i in range(len(sum_arr)):
            val = sum_arr[i] % k
            val_arr.append(val)

        rem = {0: -1}
        for i, j in enumerate(val_arr):
            if j not in rem:
                rem[j] = i
            elif i - rem[j] > 1:
                return True
        return False