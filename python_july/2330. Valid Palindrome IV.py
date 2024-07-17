class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        if n < 3:
            return True
        
        l, r = 0, n-1
        cnt = 0
        while l < r:
            if s[l] != s[r]:
                cnt +=1
            l += 1
            r -= 1
        
        return 0 <= cnt < 3
            