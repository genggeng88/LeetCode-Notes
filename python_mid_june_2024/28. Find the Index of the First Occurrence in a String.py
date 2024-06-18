class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, k = len(haystack), len(needle)
        for i in range(n):
            if haystack[i: i+k] == needle:
                return i
        return -1