class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        maxNum = max(nums)
        n = len(nums)
        cnts = [0] * (maxNum + n)

        for num in nums:
            cnts[num] += 1
        
        res = 0
        for i in range(maxNum + n):
            if cnts[i] > 1:
                cnts[i+1] += cnts[i] - 1
                res += cnts[i] - 1
                cnts[i] = 1
        return res