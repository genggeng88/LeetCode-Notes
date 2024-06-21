class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = j = 0
        res = []
        while i < n and j < n:
            if j < n-1 and nums[j+1] != nums[j]+1:
                if j == i:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[i]) + '->' +str(nums[j]))
                i = j+1
                j = i
            else:
                j += 1
        if i == j-1:
            res.append(str(nums[i]))
        if i < j-1:
            res.append(str(nums[i]) + '->' +str(nums[j-1]))
        return res
