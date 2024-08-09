class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        ptr = self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
            ptr = ptr.children[letter]
        ptr.end = True
    
    def search(self, word):
        ptr = self.root
        prefix = ""
        for letter in word:
            if letter not in ptr.children:
                return word
            prefix += letter
            if ptr.children[letter].end == True:
                return prefix
            ptr = ptr.children[letter]
        return word