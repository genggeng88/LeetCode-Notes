class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumL = [0] * n
        sumR = [0] * n

        for i in range(1, n):
            sumL[i] = sumL[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            sumR[i] = sumR[i+1] + nums[i+1]
        for i in range(n):
            if sumL[i] == sumR[i]:
                return i
        return -1