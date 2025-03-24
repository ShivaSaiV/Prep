class Solution:
    def longestConsecutive(self, nums):
        mySet = set(nums)

        for i in mySet:
            # if start of sequence
            if (i - 1) not in mySet:
                length = 1
                while (i + length) in mySet:
                    length += 1
                longest = max(length, longest)
        
        return longest