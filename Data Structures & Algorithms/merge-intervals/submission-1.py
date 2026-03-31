class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if prev[1] >= start:
                prev = [prev[0], max(end, prev[1])]
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)

        return res