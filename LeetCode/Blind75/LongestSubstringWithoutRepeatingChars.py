class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return 0

        mySet = 0
        
        left = 0
        maxLength = 0


        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(nums[left])
                left += 1
            
            mySet.add(s[right])
            
            length = right - left + 1
            maxLength = max(length, maxLength)
        
        return maxLength

test = Solution()
print(test.lengthOfLongestSubstring("zxyxyz"))


            