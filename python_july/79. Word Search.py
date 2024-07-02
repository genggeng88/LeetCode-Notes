class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row, col, seen, current_word):
            if current_word == "":
                return True
            
            if row < 0 or row >=m or col < 0 or col >= n or board[row][col] != current_word[0] or (row, col) in seen:
                return False
            
            seen.add((row, col))
            found = (backtrack(row, col+1, seen, current_word[1:]) or
                     backtrack(row, col-1, seen, current_word[1:]) or
                     backtrack(row+1, col, seen, current_word[1:]) or
                     backtrack(row-1, col, seen, current_word[1:]))
            seen.remove((row, col))
            
            return found

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, set(), word):
                        return True
        
        return False