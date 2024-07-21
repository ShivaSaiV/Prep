class Solution(object):
    def compress(self, chars):

        res = 0
        num = 0

        if len(chars) == 0:
            return 0
        
        if len(chars) == 1:
            return 1
        
        while num < len(chars):
            # count = chars.count(chars[num])
            # chars[res] = chars[num]

            l = chars[num]
            count = 0

            while ((num < len(chars)) and (l == chars[num])):
                num += 1
                count += 1

            chars[res] = l
            res += 1
            

            if count > 1:
                for i in str(count):
                    chars[res] = i
                    res += 1


        print(chars)


        return res
    
test = Solution()
print(test.compress(["a","a","b","b","c","c","c"]))
print(test.compress(["a"]))
print(test.compress(["a","a","a","b","b","a","a"]))
