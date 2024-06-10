class Solution(object):
    def subarraysDivByK(self, nums, k):
        total = 0
        count = 0
        prefix = {0: 1}
        rem = 0
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k

            if rem < 0:
                rem += k

            if rem in prefix:
                count += prefix[rem]
                prefix[rem] += 1

            else:
                prefix[rem] = 1

        return count
        