class Solution(object):
    def mergeAlternately(self, word1, word2):
        comb = []
        start = 0
        while start < len(word1) or start < len(word2):
            if start < len(word1):
                comb.append(word1[start])
            if start < len(word2):
                comb.append(word2[start])
            start += 1
            

        return "".join(comb)
        