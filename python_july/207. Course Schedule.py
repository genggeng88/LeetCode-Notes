class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [ 0 for _ in range(numCourses)]
        nei = [[] for _ in range(numCourses)]
        
        for pre in prerequisites:
            nei[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        idx = 0
        while queue:
            idx += 1
            node = queue.popleft()
            for n in nei[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        
        return idx == numCourses
