# https://leetcode.com/problems/ransom-note/
# Difficulty: Easy

# Given two strings ransomNote and magazine, return true if 
# ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        myDict = {}
        res = 0

        for i in magazine:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        for i in ransomNote:
            if i in myDict:
                if myDict[i] >= 1:
                    res += 1
                    myDict[i] -= 1

        return res == len(ransomNote)

test = Solution()
print(test.canConstruct("a", "aab"))
print(test.canConstruct("a", "b"))