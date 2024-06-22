class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        m, n = len(pattern), len(slist)
        seen = dict()

        if m != n:
            return False
        
        for i in range(n):
            if pattern[i] in seen:
                if seen[pattern[i]] != slist[i]:
                    return False
            else:
                if slist[i] in list(seen.values()):
                    return False
                seen[pattern[i]] = slist[i]
        return True