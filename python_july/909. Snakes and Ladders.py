class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)

        def get_val(k):
            rows, res = divmod(k-1, n)
            r = n-1-rows
            c = res if rows%2 == 0 else n-1-res
            return board[r][c]

        visited = set([1])
        queue = deque([(1, 0)])

        while queue:
            curr, moves = queue.popleft()
            for next_cell in range(curr+1, curr+7):
                if next_cell <= n*n:
                    dest = get_val(next_cell)
                    if dest != -1:
                        next_cell = dest
                    if next_cell == n*n:
                        return moves+1
                    if next_cell not in visited:
                        visited.add(next_cell)
                        queue.append((next_cell, moves+1))
        
        return -1
