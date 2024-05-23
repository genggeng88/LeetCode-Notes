class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        inf = -float('inf')
        nums = [inf] + nums + [inf]

        n = len(nums)
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1

        return -1