class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        neighbors = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            indegree[pre[0]] += 1
            neighbors[pre[1]].append(pre[0])
        
        queue = deque()
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        idx = 0
        while queue:
            node = queue.pop()
            idx += 1
            res.append(node)
            for nei in neighbors[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return res if idx == numCourses else []