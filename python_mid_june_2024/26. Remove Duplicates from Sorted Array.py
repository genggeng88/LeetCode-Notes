class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        i = j = 1
        n = len(nums)
        if n == 1:
            return 1
        while i < n and j < n:
            if nums[j] == prev:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                prev = nums[i]
                i += 1
                j += 1
        return i