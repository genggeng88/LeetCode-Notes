class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        
        while left <= right:
            tmp = left**2 + right**2
            if tmp == c:
                return True
            elif tmp < c:
                left -= 1
            else:
                right -= 1
        return False