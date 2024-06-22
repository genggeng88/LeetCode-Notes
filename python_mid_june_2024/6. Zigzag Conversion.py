class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        goingDown = False
        strs = [''] * numRows
        row = 0

        for char in s:
            strs[row] += char
            if row == 0 or row == numRows-1:
                goingDown = not goingDown
            row += 1 if goingDown else -1
        
        return "".join(strs)