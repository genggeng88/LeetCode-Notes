class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        i = n-1
        
        while i >= 0:
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            i -= 1
        
        return max(dp)