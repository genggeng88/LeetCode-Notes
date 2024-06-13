class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1
        
        max_diff_remain = [0]*n
        max_diff = 0

        for i in range(n-1, -1, -1):
            max_diff = max(max_diff, jobDifficulty[i])
            max_diff_remain[i] = max_diff

        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return max_diff_remain[i]
            
            best = float('inf')
            hardest = 0
            for j in range(i, n-(d-day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j+1, day+1))
            return best
        
        return dp(0, 1)