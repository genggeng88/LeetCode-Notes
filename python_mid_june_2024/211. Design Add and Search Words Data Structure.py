class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        
    def search(self, word: str) -> bool:
        
        def helper(word, idx, node) -> bool:
            if idx == len(word):
                return node.is_end
            
            char = word[idx]
            if char == '.':
                for child in node.children.values():
                    if helper(word, idx+1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return helper(word, idx+1, node.children[char])
        
        return helper(word, 0, self.root)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)