class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        left = nums[:n-k]
        right = nums[n-k:]
        nums[:k] = right
        nums[k:] = left

        return 