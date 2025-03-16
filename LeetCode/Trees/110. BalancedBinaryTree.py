# https://leetcode.com/problems/balanced-binary-tree/description/
# Difficulty: easy

# Given a binary tree, determine if it is height-balanced.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        balanced = [True]

        def height(root):
            if not root:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight) > 1:
                balanced[0] = False
                return 0

            return 1 + max(leftHeight, rightHeight)

        height(root)
        return balanced[0]
         
        