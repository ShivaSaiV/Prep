# https://leetcode.com/problems/longest-common-prefix/
# Difficulty: easy

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        
        i = 0
        lengths = []
        for word in strs:
            lengths.append(len(word))
        print(lengths)
        minLen = min(lengths)
        while (i < minLen):
            for s in strs:
                # print(s[i])
                # print("Hey")
                print(strs[0][i])
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0][:i]

test = Solution()
print(test.longestCommonPrefix(["flower","flow","flight"]))
print(test.longestCommonPrefix(["c","acc","ccc"]))
