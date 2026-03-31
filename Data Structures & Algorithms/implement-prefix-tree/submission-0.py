class TreeNode:
    def __init__(self):
        self.node = {}
        self.word = False
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        base = self.root
        for char in word:
            if char not in base.node:
                base.node[char] = TreeNode()
            base = base.node[char]
        # Reached the last node, set it to true for word
        base.word = True


    def search(self, word: str) -> bool:
        base = self.root
        for char in word:
            if char not in base.node:
                return False
            base = base.node[char]
        
        # Check if thats a word in Trie
        return base.word

    def startsWith(self, prefix: str) -> bool:
        base = self.root
        for char in prefix:
            if char not in base.node:
                return False
            base = base.node[char]
        
        return True
        
        