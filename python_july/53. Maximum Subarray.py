class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = global_max = nums[0]
        n = len(nums)

        for i in range(1, n):
            current_max = max(nums[i], current_max+nums[i])
            if current_max > global_max:
                global_max = current_max
        
        return global_max