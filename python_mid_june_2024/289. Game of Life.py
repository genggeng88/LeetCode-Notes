class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        lives = [[0 for _ in range(n)] for _ in range(m)]
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    for nei in neighbors:
                        new_row = i + nei[0]
                        new_col = j + nei[1]
                        if 0 <= new_row <= m-1 and 0 <= new_col <= n-1:
                            lives[new_row][new_col] += 1
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if lives[i][j] == 2 or lives[i][j] == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if lives[i][j] == 3:
                        board[i][j] = 1