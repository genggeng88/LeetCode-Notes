class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        rightMax = [0] * n
        suffix = rightMax[n-1] = nums[n-1]
        current_max = normal_max = nums[0]
        prefix = 0
        special_max = nums[0]

        for i in range(n-2, 0, -1):
            suffix += nums[i]
            rightMax[i] = max(suffix, rightMax[i+1])

        for i in range(1, n):
            current_max = max(nums[i], current_max+nums[i])
            normal_max = max(normal_max, current_max)
            prefix += nums[i-1]
            special_max = max(special_max, prefix + rightMax[i])
        
        return max(normal_max, special_max)
