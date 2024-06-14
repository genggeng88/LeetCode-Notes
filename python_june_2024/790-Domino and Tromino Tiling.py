class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        if n < 3:
            return n
        
        f = [0]*(n+1)
        p = [0]*(n+1)

        f[1] = 1; f[2] = 2; p[2] = 1

        for i in range(3, n+1):
            f[i] = (f[i-2] + f[i-1] + 2*p[i-1]) % MOD
            p[i] = (p[i-1] + f[i-2]) % MOD
        
        return f[n]