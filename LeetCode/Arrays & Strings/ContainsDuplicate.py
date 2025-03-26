class Solution:
    def hasDuplicate(self, nums):
        mySet = set()
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        
        return False

test = Solution()
print(test.hasDuplicate([1, 2, 3, 3]))
         