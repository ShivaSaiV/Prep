# https://leetcode.com/problems/first-bad-version/description/
# Difficulty: easy

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n

        while l < r:
            m = l + ((r - l) // 2)

            if self.isBadVersion(m) == False:
                l = m + 1
            else:
                r = m

            print(l)
        
        return l

    def isBadVersion(self, m):
        arr = [False, False, False, True, True]
        return arr[m]

test = Solution()
print(test.firstBadVersion(5))