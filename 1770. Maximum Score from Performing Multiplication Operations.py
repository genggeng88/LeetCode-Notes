class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        memo = {}
        for left in range(0, m+1):
            memo[(m, left)] = 0
        
        for op in range(m-1, -1, -1):
            for left in range(0, op+1):
                right = n-1-(op-left)
                memo[(op, left)] = max(nums[left]*multipliers[op] + memo[(op+1, left+1)], nums[right]*multipliers[op] + memo[(op+1, left)])

        return memo[(0, 0)]