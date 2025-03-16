# https://leetcode.com/problems/diameter-of-binary-tree/description/
# Difficulty: easy

'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''

class Solution(object):
    def diameterOfBinaryTree(self, root):
        # d = height_left + height_right
        largestDiameter = [0]

        def height(root):
            if root is None:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)
            currDiameter = leftHeight + rightHeight

            largestDiameter[0] = max(largestDiameter[0], currDiameter)

            return 1 + max(leftHeight, rightHeight)

        height(root)
        return largestDiameter[0]
        
        
