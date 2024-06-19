import math 


class Solution(object):
    def judgeSquareSum(self, c):
        start = 0
        end = int(math.sqrt(c))
        count = 0
        while (start <= end):
            sumSquares = (start * start) + (end * end)
            print(sumSquares)
            if (sumSquares == c):
                return True
                count += 1
            elif sumSquares > c:
                end -= 1
            else:
                start += 1
            
        if count > 0:
            return True
        else:
            return False
        

test = Solution()
print(test.judgeSquareSum(5))