class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        
        n = len(candies)
        res = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= maxnum:
                res[i] = True
        return res
