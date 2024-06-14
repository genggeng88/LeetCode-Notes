class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[None for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        def minD(word1: str, word2: str, idx1: int, idx2: int) -> int:
            if idx1 == 0:
                return idx2
            if idx2 == 0:
                return idx1
            if memo[idx1][idx2]:
                return memo[idx1][idx2]
            minE = 0
            if word1[idx1-1] == word2[idx2-1]:
                minE = minD(word1, word2, idx1-1, idx2-1)
            else:
                insertOp = minD(word1, word2, idx1, idx2-1)
                deleteOp = minD(word1, word2, idx1-1, idx2)
                replaceOp = minD(word1, word2, idx1-1, idx2-1)
                minE = min(insertOp, deleteOp, replaceOp) + 1
            memo[idx1][idx2] = minE
            return minE
            
        return minD(word1, word2, len(word1), len(word2))