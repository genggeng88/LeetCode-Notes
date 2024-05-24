class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        queue = deque()
        cnt = 0

        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1
            while queue:
                city = queue.popleft()
                for c in range(n):
                    if isConnected[city][c] and visited[c] == 0:
                        queue.append(c)
                        visited[c] = 1            

        return cnt




