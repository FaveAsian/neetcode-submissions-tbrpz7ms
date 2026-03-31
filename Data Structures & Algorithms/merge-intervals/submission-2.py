class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        prev = intervals[0]
        res = []
        for start, end in intervals:
            if start <= prev[1]:
                prev = [prev[0], max(prev[1], end)]
            else:
                res.append(prev)
                prev = [start, end]
        res.append(prev)
        return res