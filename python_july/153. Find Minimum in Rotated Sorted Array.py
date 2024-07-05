class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1

        if nums[n-1] >= nums[0]:
            return nums[0]

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid-1
