# https://leetcode.com/problems/roman-to-integer/description/
# Difficulty: Easy

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        myDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        
        start = 0
        while (start < len(s)):
            val = myDict[s[start]]
            if start + 1 < len(s):
                nextval = myDict[s[start + 1]]
            else:
                nextval = val

            if val >= nextval:
                total += val
                start += 1
            else:
                total += (nextval - val)
                start += 2


        return total


test = Solution()
print(test.romanToInt("III"))

