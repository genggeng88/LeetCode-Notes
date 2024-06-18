class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for char, count in ransom.items():
            if mag[char] < count:
                return False
        return True