class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, col, diagonal, anti_diagonal):
            if row == n:
                return 1

            ans = 0
            for c in range(n):
                if c in col or ((row + c) in anti_diagonal) or ((row -c) in diagonal):
                    continue
                
                col.add(c)
                diagonal.add(row-c)
                anti_diagonal.add(row+c)
                ans += backtrack(row+1, col, diagonal, anti_diagonal)

                col.remove(c)
                diagonal.remove(row-c)
                anti_diagonal.remove(row+c)
            return ans

        return backtrack(0, set(), set(), set())