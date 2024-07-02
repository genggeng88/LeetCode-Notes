class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, target, path):
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(idx, n):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, target-candidates[i], path)
                path.pop()
        
        ans = []
        n = len(candidates)
        backtrack(0, target, [])
        return ans