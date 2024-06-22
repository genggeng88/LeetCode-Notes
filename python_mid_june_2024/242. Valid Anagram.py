class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for char in s:
            sdict[char] += 1
        for char in t:
            tdict[char] += 1
        for item in sdict:
            if sdict[item] != tdict[item]:
                return False
        return True