class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)

        def can_finish(k):
            acc = 0
            for pile in piles:
                acc += (pile + k - 1) // k
            if acc <= h:
                return True
            return False
        
        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid+1
        return l
        