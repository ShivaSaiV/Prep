# https://leetcode.com/problems/path-sum/description/
# Difficulty: easy

'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        def traverse(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum

            return traverse(root.left, curr_sum) or traverse(root.right, curr_sum)

        return traverse(root, 0)
            