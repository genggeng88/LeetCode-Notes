class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        
        i, j, acc = 0, 0, 0
        min_length = float('inf')

        while j < n:
            acc += nums[j]
            while acc >= target:
                min_length = min(min_length, j-i+1)
                acc -= nums[i]
                i += 1
            j += 1
        
        return min_length if min_length != float('inf') else 0