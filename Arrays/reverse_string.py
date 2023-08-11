# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:

        # inbuilt function
        # print(s.reverse())

        # other method:
        start = 0
        end = len(s) - 1

        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        
