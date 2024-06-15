class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        i = 2
        while i < n:
            if nums[i-2] == nums[i-1] and nums[i-1] == nums[i]:
                break
            i += 1
        
        j = i+1
        cnt = 2
        target = nums[i-1]

        while i < n and j < n:
            if nums[j] == target and cnt == 1:
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1
                i += 1
                j += 1
            elif nums[j] == target and cnt == 2:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                target = nums[i]
                cnt = 1
                i += 1
                j += 1
        return i