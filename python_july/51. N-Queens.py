class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(tmp, row, cols, pos_diags, neg_diags):
            
            if row == n:
                tmp = ["".join(ele) for ele in tmp]
                ans.append(tmp)

            for c in range(n):
                if c in cols or c-row in pos_diags or c+row in neg_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(c-row)
                neg_diags.add(c+row)
                tmp[row][c] = "Q"

                backtrack(tmp, row+1, cols, pos_diags, neg_diags)

                cols.remove(c)
                pos_diags.remove(c-row)
                neg_diags.remove(c+row)
                tmp[row][c] = "."
        
        tmp = [['.' for j in range(n)] for i in range(n)]
        ans = []
        backtrack(tmp, 0, set(), set(), set())

        return ans