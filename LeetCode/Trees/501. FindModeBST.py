# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Difficulty: easy

class Solution(object):
    def findMode(self, root):
        if root is None:
            return 0
        myDict = {}
        def traverse(node):
            if node is None:
                return 0

            traverse(node.left)

            if node.val in myDict:
                myDict[node.val] += 1
            else:
                myDict[node.val] = 1

            traverse(node.right)

        traverse(root)

        max_val = max(myDict.values())
        res = []
        for k, v in myDict.items():
            if v == max_val:
                res.append(k)
        return res

            
        