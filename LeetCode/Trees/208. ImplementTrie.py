# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Difficulty: Medium

class Trie(object):

    def __init__(self):
        self.trie = {}
        

    def insert(self, word):
        d = self.trie

        # create a dictionary for each letter (nested dictionaries)
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        
        d["."] = "."


    def search(self, word):
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]
        
        return "." in d 
        

    def startsWith(self, prefix):
        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)