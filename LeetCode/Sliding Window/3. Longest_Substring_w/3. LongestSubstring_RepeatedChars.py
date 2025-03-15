# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium

'''
Given a string s, find the length of the longest substring without duplicate characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        maxCounter = 0
        mySet = set()

        # Loop through each character
        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            mySet.add(s[right])
            maxCounter = max(maxCounter, right - left + 1)

        return maxCounter

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))

    
