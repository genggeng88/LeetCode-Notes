class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        newS = " ".join(s[::-1])
        return newS