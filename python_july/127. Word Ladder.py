class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        beginWords = set([beginWord])
        endWords = set([endWord])
        n = len(beginWord)
        visited = set([beginWord, endWord])
        ans = 1

        while beginWords and endWords:
            if len(beginWords) > len(endWords):
                beginWords, endWords = endWords, beginWords
            
            next_set = set()
            for beginWord in beginWords:
                for i in range(n):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        next_word = beginWord[:i] + j + beginWord[i+1:]
                        if next_word in endWords:
                            return ans + 1
                        if next_word not in visited and next_word in wordList:
                            visited.add(next_word)
                            next_set.add(next_word)
            beginWords = next_set
            ans += 1
        return 0