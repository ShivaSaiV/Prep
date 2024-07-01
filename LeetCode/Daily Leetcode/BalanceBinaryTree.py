class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addChild(self, value):
        if self.value == value:
            return
        
        if self.value > value:
            if self.left:
                self.left.addChild(value)
            else:
                self.left = TreeNode(value)

        else:
            if self.right:
                self.right.addChild(value)
            else:
                self.right = TreeNode(value)

class Solution(object):
    def balanceBST(self, root):
        self.elements = []
        self.inOrder(root)
        return self.createBalanced(0, len(self.elements) - 1)
    
    def inOrder(self, node):
        if node:
            if node.left: 
                self.inOrder(node.left)
            self.elements.append(node)
            if node.right:
                self.inOrder(node.right)
            
        

    def createBalanced(self, s, e):
        if s > e:
            return None
        mid = (s + e) // 2
        node = self.elements[mid]
        node.left = self.createBalanced(s, mid - 1)
        node.right = self.createBalanced(mid + 1, e)
        return node
                
    

test = Solution()
print(test.balanceBST([1,null,2,null,3,null,4,null,null]))


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addChild(self, value):
        if self.value == value:
            return
        
        if self.value > value:
            if self.left:
                self.left.addChild(value)
            else:
                self.left = TreeNode(value)

        else:
            if self.right:
                self.right.addChild(value)
            else:
                self.right = TreeNode(value)

   
            

class Solution(object):
    def balanceBST(self, root):
        self.elements = []
        
        return self.createBalanced(0, len(self.elements) - 1)
    
    def inOrder(self, node):
        if node:
            if node.left: 
                self.inOrder(node.left)
            self.elements.append(node)
            if node.right:
                self.inOrder(node.right)
    
        

    def createBalanced(self, s, e):
        if s > e:
            return None
        mid = (s + e) // 2
        node = self.elements[mid]
        node.left = self.createBalanced(s, mid - 1)
        node.right = self.createBalanced(mid + 1, e)
        return node
                