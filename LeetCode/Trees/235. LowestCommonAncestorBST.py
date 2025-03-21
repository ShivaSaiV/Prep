# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        lca = [root]

        def search(root):
            if root is None:
                return
            
            lca[0] = root
            
            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return
        
        search(root)
        return lca[0]


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
        