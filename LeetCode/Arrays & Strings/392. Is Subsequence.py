# https://leetcode.com/problems/is-subsequence/description/
# Difficulty: Easy

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution():
    def isSubsequence(self, s, t):
        if s == t:
            return True
        if len(s) > len(t):
            return False
        
        i = 0
        j = 0

        while (i < len(t) and j < len(s)):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)

test = Solution()
print(test.isSubsequence("abc", "ahbgdc"))
print(test.isSubsequence("axe", "ahbgdc"))