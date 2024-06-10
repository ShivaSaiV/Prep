class Solution(object):
    def appendCharacters(self, s, t):
        n1, n2 = 0, 0
        while (n1 < len(s) and n2 < len(t)):
            if (s[n1] == t[n2]):
                n1 += 1
                n2 += 1
            else:
                n1 += 1
            print(n2)
        if n2 == len(t):
            return 0
        print(n2)
        return len(t) - n2
        