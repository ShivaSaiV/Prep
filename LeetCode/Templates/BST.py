# Binary tree: eevry node has at most 2 child nodes
# BST: left < and right >
# ideal:
# log(n) - insert item, search, delete
# insert all - nlog(n)
# In order = LNR
# Pre = NLR
# Post = LRN

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == value:
            return
        if self.value > value:
            # add in left sub tree
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)


        else:
            # add in right sub tree
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        
    def inOrder(self):
        elements = []

        if self.left:
            elements += self.left.inOrder()

        elements.append(self.value)

        if self.right:
            elements += self.right.inOrder()   

        return elements
    
    def preOrder(self):
        elements = []

        elements.append(self.value)

        if self.left:
            elements += self.left.preOrder()

        if self.right:
            elements += self.right.preOrder()

        return elements
    
    def postOrder(self):
        elements = []

        if self.left:
            elements += self.left.postOrder()

        if self.right:
            elements += self.right.postOrder()

        elements.append(self.value)

        return elements
    
    def search(self, val):
        if self.value == val:
            return True
        if val < self.value:
            if self.left:
                self.left.search()
            else:
                return False
            
        else:
            if self.right:
                self.right.search()
            else:
                return False



def buildTree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.insert(elements[i])
    
    return root

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    nums_tree = buildTree(nums)
    print(nums_tree.postOrder())

