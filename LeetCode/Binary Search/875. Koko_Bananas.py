# https://leetcode.com/problems/koko-eating-bananas/description/
# Difficulty: Medium

class Solution(object):
    def minEatingSpeed(self, piles, h):
        def valid(k):
            num = 0
            for i in piles:
                if i % k == 0:
                    num += i // k
                else:
                    num += (i // k) + 1
            print(num)
            if num <= h:
                return True
            return False

        n = len(piles)

        if n == h:
            return max(piles)

        l = 1
        r = max(piles)

        while l < r:
            m = l + ((r - l) // 2)

            if valid(m) == True:
                r = m 
            else:
                l = m + 1
        
        return r 

test = Solution()
print(test.minEatingSpeed([3, 6, 7, 11], 8))
        
        