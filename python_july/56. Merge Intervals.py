class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        n = len(intervals)
        i, curr = 1, intervals[0]
        res = []
        while i < n:
            if intervals[i][0] > curr[1]:
                res.append(curr)
                curr = intervals[i]
            else:
                curr = [curr[0], max(curr[1], intervals[i][1])]
            i += 1
        res.append(curr)
        return res