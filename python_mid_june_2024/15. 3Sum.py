class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(idx: int, target: int):
            i, j = idx+1, n-1
            
            while i < j:
                total = nums[i] + nums[j]
                if total == target:
                    res.append([nums[idx], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif total < target:
                    i += 1
                else:
                    j -= 1
        
        nums.sort()
        i, n = 0, len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                twoSum(i, -nums[i])
            
        return res
            