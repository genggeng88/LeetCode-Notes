class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            
            sum_square = 0
            seen.add(n)
            while n > 0:
                sum_square += (n % 10)**2
                n //= 10
            n = sum_square
