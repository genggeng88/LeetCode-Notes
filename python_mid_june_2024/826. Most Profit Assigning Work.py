class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs, key = lambda x : x[0])
        worker.sort()
        i = best = max_profit = 0

        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            max_profit += best
        return max_profit
            