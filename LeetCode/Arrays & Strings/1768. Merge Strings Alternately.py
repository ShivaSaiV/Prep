# https://leetcode.com/problems/merge-strings-alternately/description/
# Difficulty: Easy
# Strings, 2-pointers

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)

        i, j = 0, 0
        res = []
        
        while (True):
            if (i == n1 and j == n2):
                break
            if i < n1:
                res.append(word1[i])
                i += 1
            if j < n2:
                res.append(word2[j])
                j += 1
        
        return "".join(res)
    

test = Solution()
print(test.mergeAlternatively("abcde", "pqr"))