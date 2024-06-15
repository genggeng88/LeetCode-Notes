class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        nums.sort()

        while i < n and nums[i] < val:
            i += 1
        j = i
        while j < n and nums[j] <= val:
            j += 1

        nums[i:i+n-j] = nums[j:]
        
        return n+i-j
            