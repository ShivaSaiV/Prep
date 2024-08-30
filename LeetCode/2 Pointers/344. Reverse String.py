# https://leetcode.com/problems/reverse-string/
# Difficulty: easy

# Write a function that reverses a string. 
# The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            r -= 1
            l += 1
        
