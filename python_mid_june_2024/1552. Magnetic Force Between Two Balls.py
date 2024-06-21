class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def canPlaceBalls(x, m):
            i, curr = 1, position[0]
            ball_placed = 1
            while i < n:
                if position[i] - curr >= x:
                    curr = position[i]
                    ball_placed += 1
                if m == ball_placed:
                    return True
                i += 1
            return False

        position.sort()
        n = len(position)
        low, high = 1, position[-1]//(m-1) + 1
        ans = low

        while low <= high:
            mid = low + (high-low)//2
            if canPlaceBalls(mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans