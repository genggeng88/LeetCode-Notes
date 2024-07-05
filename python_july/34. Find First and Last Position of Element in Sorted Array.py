class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binary(isLeft):
            idx = -1
            i, j = 0, n-1
            while i <= j:
                mid = i + (j-i)//2
                if nums[mid] < target:
                    i = mid+1
                elif nums[mid] > target:
                    j = mid-1
                else:
                    idx = mid
                    if isLeft:
                        j = mid-1
                    else:
                        i = mid+1
            return idx

        first = binary(True)
        last = binary(False)
        if first != -1 and last != -1:
            return [first, last]
        return [-1, -1]