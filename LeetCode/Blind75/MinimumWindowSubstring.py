class Solution:
    def minWindow(self, s, t):
        if t == "":
            return ""

        if s == t:
            return s 
        
        if len(t) > len(s):
            return ""
        
        countT = {}
        window = {}

        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right] 
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update our result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        
        l, r = res 
        if resLen != float("inf"):
            return s[l : r + 1]
        else:
            return ""




