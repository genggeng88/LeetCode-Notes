class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        def border(r: int, c: int) -> bool:
            return (r == 0 or c == 0 or r == m-1 or c == n-1) and [r, c] != entrance
        
        def neighbors(r, c):
            pairs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            ans = []
            for pair in pairs:
                if 0 <= pair[0] < m and 0 <= pair[1] < n and maze[pair[0]][pair[1]] == '.':
                    ans.append((pair[0], pair[1]))
            return ans

        sr, sc = entrance[0], entrance[1]
        queue = deque([(sr, sc, 0)])
        visited = set([(sr, sc)])

        while queue:
            r, c, steps = queue.popleft()
            for nr, nc in neighbors(r, c):
                if (nr, nc) not in visited:
                    if border(nr, nc):
                        return steps + 1
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))
        
        return -1