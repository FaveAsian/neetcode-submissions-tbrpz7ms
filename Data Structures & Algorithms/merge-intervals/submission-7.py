class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        
        intervals.sort(key=lambda x: x[0])
        
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                stack[-1][0] = min(intervals[i][0], stack[-1][0])
                stack[-1][1] = max(intervals[i][1], stack[-1][1])
            else:
                stack.append(intervals[i])

        return stack