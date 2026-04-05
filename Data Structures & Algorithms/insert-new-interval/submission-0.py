class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        idx = 0
        # add intervals before new
        while idx < len(intervals):
            start, end = intervals[idx]

            if end < newInterval[0]:
                res.append(intervals[idx])
                idx += 1
            else:
                break

        # merge those after new
        while idx < len(intervals):
            start, end = intervals[idx]

            # check if new interval can be merged
            if start <= newInterval[1]:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            else:
                break
            idx += 1
        res.append(newInterval)
        # add remaining
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1
        
        return res
