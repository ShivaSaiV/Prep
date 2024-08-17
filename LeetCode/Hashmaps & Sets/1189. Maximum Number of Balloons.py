# https://leetcode.com/problems/maximum-number-of-balloons/description/
# Difficulty: Easy

# Given a string text, you want to use the characters of text to form 
# as many instances of the word "balloon" as possible.
# You can use each character in text at most once. 
# Return the maximum number of instances that can be formed.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        myDict = {}

        for i in text:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        req = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }

        res = 0

        condition = True

        while (condition):
            for i in req:
                if i in myDict and myDict[i] >= req[i]:
                    myDict[i] -= req[i]
                else:
                    condition = False
                    break

            if condition:
                res += 1
        
        return res
        

test = Solution()
# print(test.maxNumberOfBalloons("nlaebolko"))
print(test.maxNumberOfBalloons("loonbalxballpoon"))
# print(test.maxNumberOfBalloons("leetcode"))