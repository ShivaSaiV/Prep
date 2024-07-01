class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def insert(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printTree(self):
        spaces = " " * self.getLevel() * 4
        prefix = spaces + "|__"
        if self.parent:
            print(prefix + self.value)
        else:
            print(spaces + self.value)
        if len(self.children) > 0:
            for child in self.children:
                child.printTree()
        

def build_product_tree():
    root = TreeNode("Technology")

    laptop = TreeNode("Laptop")
    laptop.insert(TreeNode("Surface"))
    laptop.insert(TreeNode("Macbook"))
    phone = TreeNode("Phone")

    

    root.insert(laptop)
    root.insert(phone)

    
    
    

    return root



if __name__ == "__main__":
    root = build_product_tree()
    root.printTree()

    
