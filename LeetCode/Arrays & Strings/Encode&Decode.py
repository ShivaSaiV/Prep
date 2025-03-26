class Solution():
    def encode(self, strs):
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i 
        return res 
    
    def decode(self, s):
        res = []
        i = 0

        # each iteration will read 1 word
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res

