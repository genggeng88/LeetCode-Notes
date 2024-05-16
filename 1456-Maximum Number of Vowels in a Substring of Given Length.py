class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cnts = [0]*(n-k+1)
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        i,cnt = 0, 0
        while i < k:
            if s[i] in vowels:
                cnt +=1
            i += 1
        
        cnts[0] = cnt 

        for i in range(1, n-k+1):
            cnt2 = cnts[i-1]
            if s[i-1] in vowels:
                cnt2 -= 1
            if s[i+k-1] in vowels:
                cnt2 += 1
            cnts[i] = cnt2
        
        return max(cnts)