# https://leetcode.com/problems/valid-anagram/description/
# Difficulty: easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        myDict = {}

        if len(s) != len(t):
            return False

        for i in t:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1
        print(myDict)

        res = 0

        for i in s:
            if i in myDict:
                if myDict[i] >= 1:
                    res += 1
                    myDict[i] -= 1

        print(myDict)
            

        return res == len(t)
        
test = Solution()
print(test.isAnagram("anagram", "nagaram"))
print(test.isAnagram("rat", "cat"))
print(test.isAnagram("aacc", "ccac"))
