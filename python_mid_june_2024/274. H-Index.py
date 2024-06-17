class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = max(citations)
        indices = [0] * (n+1)

        for citation in citations:
            indices[citation] += 1
        
        citation_sum = 0
        for i in range(n, 0, -1):
            citation_sum += indices[i]
            if citation_sum >= i:
                return i
        return 0
