class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(start = 1, end = n, k = k, path = []):
            if k == 0:
                ans.append(path)
                return
            for i in range(start, end - k + 2):
                backtrack(i + 1, end, k - 1, path + [i])
                
        ans = []
        backtrack()
        return ans