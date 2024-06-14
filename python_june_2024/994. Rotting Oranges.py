class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxMinute = 0
        queue = deque()
        fresh = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
        if fresh == 0:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, t = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append([nr, nc, t + 1])
                    fresh -= 1
                    maxMinute = max(maxMinute, t + 1)
        if not fresh:
            return maxMinute
        return -1