class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]
        queue = deque([0])
        n = len(rooms)

        while queue:
            key = queue.popleft()
            if key not in visited:
                visited.append(key)
            for el in rooms[key]:
                if el not in visited:
                    queue.append(el)

        return len(visited) == n