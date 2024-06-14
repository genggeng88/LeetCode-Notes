class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while a>0 or b>0 or c>0:
            a_ = a & 1; b_ = b & 1; c_ = c & 1
            if c_ == 0:
                if a_ == 1 and b_ == 1:
                    cnt += 2
                elif a_ == 1 or b_ == 1:
                    cnt += 1
            else:
                if a_ == 0 and b_ == 0:
                    cnt += 1
            
            a = a>>1; b = b>>1; c = c>>1
        return cnt