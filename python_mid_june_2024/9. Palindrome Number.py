class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if 0 <= x < 10:
            return True
        
        reversedNum = 0
        num = x
        while num > 0:
            res = num%10
            reversedNum = reversedNum*10 + res
            num //= 10

        return reversedNum == x