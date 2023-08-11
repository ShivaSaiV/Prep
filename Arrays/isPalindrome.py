class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        # Remove special characters and spaces
        for char in s:
            if char.isalnum():
                st.append(char.lower())
                
        return st == st[::-1]
