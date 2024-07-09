class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, row, col, path):
            if node.isWord:
                ans.add(path)
                node.isWord = False
            
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '#':
                return 
            
            char = board[row][col]
            if char not in node.children:
                return

            board[row][col] = '#'
            for dr, dc in directions:
                dfs(node.children[char], row+dr, col+dc, path+char)
            board[row][col] = char


        trie = Trie()
        ans = set()
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                dfs(trie.root, i, j, "")
        
        return list(ans)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] =TrieNode()
            node = node.children[char]
        node.isWord = True