class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def can_place(d, i, j):
            return not (rows[i][d] or cols[j][d] or boxes[box_index(i, j)][d])

        def place_number(d, i, j):
            board[i][j] = str(d)
            rows[i][d] = True
            cols[j][d] = True
            boxes[box_index(i, j)][d] = True

        def place_next_number(row, col):
            if col == N-1 and row == N-1:
                sudoku_solved[0] = True
            else:
                if col == N-1:
                    backtrack(row+1, 0)
                else:
                    backtrack(row, col+1)
        
        def remove_number(d, row, col):
            rows[row][d] = False
            cols[col][d] = False
            boxes[box_index(row, col)][d] = False
            board[row][col] = "."

        def backtrack(row=0, col=0):
            if board[row][col] == ".":
                for d in range(1, 10):
                    if can_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if sudoku_solved[0]:
                            return
                        remove_number(d, row, col)
            else:
                place_next_number(row, col)


        n = 3
        N = n*n
        box_index = lambda row, col: (row//n) * n + col // n

        rows = [[False] * (N+1) for _ in range(N)]
        cols = [[False] * (N+1) for _ in range(N)]
        boxes = [[False] * (N+1) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = [False]
        backtrack()