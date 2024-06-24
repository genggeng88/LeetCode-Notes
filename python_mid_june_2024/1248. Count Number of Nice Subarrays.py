class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        acc = 0
        cnt = 0
        prefix = {acc : 1}

        for num in nums:
            acc += num % 2
            if acc - k in prefix:
                cnt += prefix[acc-k]
            prefix[acc] = prefix.get(acc, 0) + 1
        return cnt