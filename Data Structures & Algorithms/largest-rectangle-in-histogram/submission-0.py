class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][-1]:
                prev_i, prev_height = stack.pop()
                res = max(res, prev_height*(i-prev_i))
                start = prev_i

            stack.append((start, height))
        print(stack)
        print(res)
        # Process rest of stack
        for i, h in stack:
            res = max(res, h*(len(heights)-i))

        return res