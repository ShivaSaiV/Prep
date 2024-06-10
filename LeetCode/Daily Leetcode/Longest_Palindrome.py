class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        counter = 0
        odds = 0

        n = len(s)
        if n == 1:
            return 1
        
        for i in range(n):
            count[s[i]] = s.count(s[i])
        # print(count)
        for i in count.values():
            if i % 2 == 0:
                counter += i
            else:
                odds += 1
        # print(counter)
        # print(odds)
        if odds > 1:
            return n - odds + 1
        elif odds == 1:
            return n
        else:
            return counter