class Solution:
    def threeSum(self, nums):
        if nums is None:
            return None
        
        res = []

        nums.sort()

        for i in range(len(nums)):
            # We don't want to use the same value twice (skips repetition)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[i] + nums[r] == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1

                    # We don't want to use the same value twice (skips repetition)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
        
        return res
