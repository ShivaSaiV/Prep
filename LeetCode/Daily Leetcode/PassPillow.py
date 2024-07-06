class Solution(object):
    def passThePillow(self, n, time):
        if time < n:
            return time + 1
        
        else:
            dir = 1
            i = 1
            for k in range(time):
                i += dir
                if i == n:
                    dir = -1
                if i == 1:
                    dir = 1          

    
        return i
    

test = Solution()
print(test.passThePillow(4, 5))