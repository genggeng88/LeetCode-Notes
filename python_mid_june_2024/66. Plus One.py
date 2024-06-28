class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(c) for c in digits])) + 1
        return [int(d) for d in str(num)]