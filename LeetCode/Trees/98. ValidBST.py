# https://leetcode.com/problems/validate-binary-search-tree/description/
# Difficulty: Medium

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        if root is None:
            return False

        myArr = []

        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)

            myArr.append(root.val)

            traverse(root.right)

        traverse(root)

        for i in range(len(myArr) - 1):
            if myArr[i] >= myArr[i + 1]:
                return False
        
        return True

