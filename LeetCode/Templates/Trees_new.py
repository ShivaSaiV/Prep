# Binary Trees

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    
# Pre-order Traversal (DFS) Time: O(n), Space: O(n) - NLR
def preOrder(node):
    if node is None:
        return
    print(node)
    preOrder(node.left)
    preOrder(node.right)

# In-order Traversal : LNR
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    print(node)
    inOrder(node.right)

# Post-order: LRN
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node)


# Iterative Pre-order (DFS) Time: O(n), Space: O(n)
def preOrder_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)

    
# Level Order Traversal (BFS): Time: O(n), Space: O(n)
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# Check if a Value exists (DFS) Time: O(n), Space: O(n)
def search(node, target):
    if not node:
        return False

    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)


# Check if value exists in BST
def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True

    if target < node.val:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)





    