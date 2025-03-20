# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Difficulty: medium

'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST - in-order is already sorted: LNR
class Solution(object):
    def kthSmallest(self, root, k):
        if root is None:
            return 

        myArr = []

        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)

            myArr.append(root.val)

            traverse(root.right)

        traverse(root)
        print(myArr)
        if k > len(myArr):
            return
        return myArr[k - 1]

        


            
        