class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        als = [0]*(n+1)
        als[0] = 0

        for i in range(1, n+1):
            als[i] = als[i-1] + gain[i-1]

        return max(als)