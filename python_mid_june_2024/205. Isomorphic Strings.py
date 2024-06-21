class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in seen:
                if seen[s[i]] != t[i]:
                    return False
            else:
                if t[i] in list(seen.values()):
                    return False
                else:
                    seen[s[i]] = t[i]
        return True