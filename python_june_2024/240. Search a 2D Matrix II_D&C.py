class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        def reduce(left, right, top, down):
            if left > right or top > down:
                return False
            if matrix[top][left] > target or matrix[down][right] < target:
                return False
            mid = left + (right - left) // 2
            row = top
            while row <= down and matrix[row][mid] <= target:
                if target == matrix[row][mid]:
                    return True
                row += 1
            return reduce(mid+1, right, top, row-1) or reduce(left, mid-1, row, down)
        return reduce(0, n-1, 0, m-1)