class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res, n = [], len(intervals)
        start, end = intervals[0][0], intervals[0][1]
        i = 1
        while i < n:
            if end < intervals[i][0]:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])
        return res 
