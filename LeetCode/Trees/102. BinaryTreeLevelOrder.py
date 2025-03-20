# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: medium

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        # BFS
        
        myQueue = deque()
        myQueue.append(root)

        res = []

        while myQueue:
            level = []
            n = len(myQueue)
            for i in range(n):
                node = myQueue.popleft()
                level.append(node.val)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)

            res.append(level)

        return res
