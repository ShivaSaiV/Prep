class Solution:
    def twoSum(self, nums, target):
        myDict = {} # val: idx
        
        for i in range(len(nums)):
            if target - nums[i] in myDict:
                return [myDict[target - nums[i]], i]
            else:
                myDict[nums[i]] = i
        return

        

