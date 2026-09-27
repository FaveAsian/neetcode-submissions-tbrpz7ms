class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for idx, height in enumerate(heights):
            # keep adding if its increasing
            # pop if below
            # store the index
            while stack and heights[stack[-1]] > height:
                mid = stack.pop()
                h = heights[mid]
                if stack:
                    length = idx - stack[-1] - 1
                else:
                    length = idx
                res = max(res, length*h)
            stack.append(idx)
            res = max(res, height)
        
        n = len(heights)
        while stack:
            mid = stack.pop()
            h = heights[mid]
            length = n - stack[-1] - 1 if stack else n
            res = max(res, length * h)

        return res