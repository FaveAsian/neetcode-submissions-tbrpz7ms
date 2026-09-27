class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights.append(0)
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

        return res