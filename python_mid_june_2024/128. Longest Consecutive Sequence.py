class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if num-1 not in nums_set:
                curr = num
                streak = 1

                while curr+1 in nums_set:
                    curr += 1
                    streak += 1
                longest_streak = max(longest_streak, streak)
        return longest_streak