class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        cnt = 1
        end = points[0][1]

        for p in points:
            if p[0] > end:
                cnt += 1
                end = p[1]
        
        return cnt