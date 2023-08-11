# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        # Remove special characters and spaces
        for char in s:
            if char.isalnum():
                st.append(char.lower())
                
        return st == st[::-1]
