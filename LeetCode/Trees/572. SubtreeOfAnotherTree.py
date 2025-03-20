# https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: easy

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        
        def sameTree(r, sr):
            if r is None and sr is None:
                return True
            
            if r:
                if not sr:
                    return False
            
            if sr:
                if not r:
                    return False

            if r.val != sr.val:
                return False

            return sameTree(r.left, sr.left) and sameTree(r.right, sr.right)

        def has_subtree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)


