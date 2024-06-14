class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        s1 = 1000000000
        s2 = 1000000000
        start = 0
        while (start < n):
            if nums[start] <= s1:
                s1 = nums[start]
            elif nums[start] <= s2:
                s2 = nums[start]
            else:
                return True

            start += 1
        
test = Solution()
print(test.increasingTriplet([20,100,10,12,5,13]))
