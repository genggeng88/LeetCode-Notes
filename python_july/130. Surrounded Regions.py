class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            if board[row][col] != "O":
                return
            board[row][col] = 'E'
            if row-1 >= 0:
                dfs(row-1, col)
            if row+1 < ROWS:
                dfs(row+1, col)
            if col-1 >= 0:
                dfs(row, col-1)
            if col+1 < COLS:
                dfs(row, col+1)

        borders = list(product(range(ROWS), [0, COLS-1]))+list(product([0, ROWS-1], range(COLS)))

        for row, col in borders:
            dfs(row, col)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'   