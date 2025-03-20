# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Difficulty: Medium

'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):

        myArr = []
        
        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            myArr.append(root.val)
            traverse(root.right)

        traverse(root)

        minAbsDist = 10**5
        
        left = 0
        right = 1

        while (right < len(myArr)):
            minDist = myArr[right] - myArr[left]
            minAbsDist = min(minDist, minAbsDist)

            left += 1
            right += 1
        
        return minAbsDist


        