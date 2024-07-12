class Solution:
    def partitionString(self, s: str) -> int:
        l, r, cnt = 0, 1, 1
        n = len(s)

        while l < n and r < n:
            substring = s[l:r]
            if s[r] in substring:
                l = r
                cnt += 1
            r += 1

        return cnt