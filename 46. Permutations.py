class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        if n == 1:
            return [nums]
        
        def backtrack(res, path):
            if not res or (path and len(path) == n):
                ans.append(path)
                return
            for i in res:
                new_res = res[:]
                new_res.remove(i)
                new_path = path + [i]
                backtrack(new_res, new_path)
        
        backtrack(nums, [])
        return ans