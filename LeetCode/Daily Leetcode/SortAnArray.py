class Solution(object):
    def sortArray(self, nums):
        n = len(nums)
        for i in range(n//2, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

        return nums
        
        
        
    def heapify(self, nums, n, i):
        maximum = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and nums[maximum] < nums[l]:
            maximum = l

        if r < n and nums[maximum] < nums[r]:
            maximum = r

        if maximum != i:
            nums[i], nums[maximum] = nums[maximum], nums[i]
            self.heapify(nums, n, maximum)
        

test = Solution()
print(test.sortArray([5,1,1,2,0,0]))



