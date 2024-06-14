class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                path[i][j] = path[i+1][j] + path[i][j+1]
        
        return path[0][0]