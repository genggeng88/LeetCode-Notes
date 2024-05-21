class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        pre = ""
        for p in products:
            trie.insert(p)
        for s in searchWord:
            pre += s
            res.append(trie.get_suggestion(pre))
        return res


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
                node.suggestions.sort()
            else:
                 if word < node.suggestions[-1]:
                    node.suggestions[-1] = word
                    node.suggestions.sort()
            
    def get_suggestion(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.suggestions
            
