class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, zeros, cnt = 0, 0, 0, 0

        while right < n:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            cnt = max(cnt, right-left+1)
            right += 1
        
        return cnt