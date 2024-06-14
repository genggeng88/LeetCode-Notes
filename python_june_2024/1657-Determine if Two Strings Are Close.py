class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        d1 = {i : word1.count(i) for i in set(word1)}
        d2 = {i : word2.count(i) for i in set(word2)}

        if sorted(list(d1.keys())) != sorted(list(d2.keys())):
            return False

        if sorted(list(d1.values())) != sorted(list(d2.values())):
            return False
        
        return True