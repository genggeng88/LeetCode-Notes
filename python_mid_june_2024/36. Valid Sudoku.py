class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cells = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                cell_idx = (i//3)*3 + j//3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in cells[cell_idx]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                cells[cell_idx].add(board[i][j])
        return True