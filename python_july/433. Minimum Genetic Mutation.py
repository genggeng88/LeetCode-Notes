class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def checkMutation(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
            return cnt == 1

        stack = deque([(startGene, 0)])
        visited = set([startGene])
        while stack:
            currGene, curr_mutation = stack.popleft()
            for gene in bank:
                if gene not in visited and checkMutation(currGene, gene):
                    if gene == endGene:
                        return curr_mutation+1
                    visited.add(gene)
                    stack.append((gene, curr_mutation+1))
        return -1
