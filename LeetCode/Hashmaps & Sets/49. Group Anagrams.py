# https://leetcode.com/problems/group-anagrams/
# Difficulty: medium

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all 
# the original letters exactly once.
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        myDict = defaultdict(list)
        for i in strs:
            word = sorted(i)
            key = "".join(word)
            myDict[key].append(i)

        return myDict.values()

test = Solution()
print(test.groupAnagrams("a, bdg, eff, a"))


class Solution2(object):
    def groupAnagrams(self, strs):
        myDict = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            myDict[key].append(i)

        return myDict.values()
