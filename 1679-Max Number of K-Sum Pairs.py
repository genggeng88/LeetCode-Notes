class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = dict()
        cnt = 0

        for i in range(n):
            need = k - nums[i]
            if need in seen:
                seen[need] -= 1
                cnt += 1
                if seen[need] == 0:
                    seen.pop(need)
            elif nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        
        return cnt