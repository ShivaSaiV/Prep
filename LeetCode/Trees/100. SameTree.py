# https://leetcode.com/problems/same-tree/
# Difficulty: easy

'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

class Solution(object):
    def isSameTree(self, p, q):
        if q is None and p is None:
            return True
        
        if q is None:
            if p:
                return False
        
        if p is None:
            if q:
                return False

        if q:
            if p is None:
                return False
        
        if p:
            if q is None:
                return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
