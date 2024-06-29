class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def turn():
            # inverse rows
            up, down = 0, m-1
            while up < down:
                mat[up], mat[down] = mat[down], mat[up]
                up += 1
                down -= 1
            
            for i in range(m):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        m, n = len(mat), len(mat[0])
        if mat == target:
            return True
        for _ in range(3):
            turn()
            if mat == target:
                return True
        return False