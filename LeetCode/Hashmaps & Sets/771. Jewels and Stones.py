# https://leetcode.com/problems/jewels-and-stones/description/
# Difficulty: Easy

# You're given strings jewels representing the types of stones that are jewels, 
# and stones representing the stones you have. Each character in stones is a type of stone you have. You want to 
# know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a 
# different type of stone from "A".

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hashSet = set(jewels)
        counter = 0
        for i in stones:
            if i in hashSet:
                counter += 1
        return counter

test = Solution()
print(test.numJewelsInStones("aA", "aAAbbbb"))