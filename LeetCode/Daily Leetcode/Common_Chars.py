from collections import Counter


class Solution(object):
    def commonChars(self, words):
        first = Counter(words[0])
        n = len(words)
        for i in range(1, n):
            if i == 1:
                combined = first
            count = Counter(words[i])
            combined = combined & count
        common = list(combined.elements())
        return common
            