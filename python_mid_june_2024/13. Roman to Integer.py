class Solution:
    def romanToInt(self, s: str) -> int:
        normals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        prevalue = 0
        for c in reversed(s):
            b = normals[c]
            if b >= prevalue:
                ans += b
            else:
                ans -= b
            prevalue = b
        return ans