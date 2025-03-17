# https://leetcode.com/problems/symmetric-tree/description/
# Difficulty: easy

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution(object):
    def isSymmetric(self, root):
        def isSameTree(p, q):
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

            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root, root)