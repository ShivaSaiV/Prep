# https://leetcode.com/problems/valid-palindrome/description/
# Difficulty: Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        newS = []
        for i in s:
            if i.isalnum():
                newS.append(i.lower())
        newS = "".join(newS)
        left = 0
        right = len(newS) - 1
        while left <= right:
            if newS[left] == newS[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
    
test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panama"))