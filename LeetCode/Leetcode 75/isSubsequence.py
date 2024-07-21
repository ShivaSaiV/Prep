class Solution():
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while (i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        print(i)
        print(j)

        if i == len(s):
            return True
        else:
            return False

test = Solution()
print(test.isSubsequence("abc", "ahbgdc"))