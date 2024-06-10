class Solution(object):
    def singleNumber(self, nums):
        arr = [0, 0]
        
        num1 = 0
        for i in range(len(nums)):
            num1 = num1 ^ nums[i]
        
        lowest = num1 & -num1

        for i in range(len(nums)):
            if (lowest & nums[i]) == 0:
                arr[0] = arr[0] ^ nums[i]
            else:
                arr[1] = arr[1] ^ nums[i]
        

        return arr
            
            
        