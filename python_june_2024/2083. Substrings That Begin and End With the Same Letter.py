class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = res = len(s)
        seen = defaultdict(int)

        for char in s:
            seen[char] += 1
        
        for c in seen.keys():
            res += int(seen[c]*(seen[c]-1)/2)
        
        return res