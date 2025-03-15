# Image compression technique
# aaaabbccc
# 4a2b3c
# Cannot use hashset because order matters

class Solution(object):
    def compression(self, input_str):
        if len(input_str) == 0:
            return ""

        count_array = []

        counter = 0
        prevChar = ""

        for i in input_str:
            if i == prevChar:
                counter += 1
            else:
                if (prevChar != ""):
                    count_array.append(counter)
                    count_array.append(prevChar)

                prevChar = i 
                counter = 1
        count_array.append(counter)
        count_array.append(prevChar)

        res = ""
        for i in count_array:
            res+=str(i)

        return res



test = Solution()
print(test.compression("aaaabbcca"))