# https://leetcode.com/problems/valid-perfect-square/description/
# Difficulty: easy

'''
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
'''

class Solution(object):
    def isPerfectSquare(self, num):
        l = 1
        r = num

        while l <= r:
            mid = l + ((r - l) // 2)

            if mid * mid == num:
                return True
            
            if mid * mid > num:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False