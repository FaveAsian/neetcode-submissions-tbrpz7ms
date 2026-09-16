class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        idx = 1

        while idx <= (n*n):
            # move right
            for i in range(left, right+1):
                res[top][i] = idx
                idx += 1
            top += 1
            # move down
            for i in range(top, bottom+1):
                res[i][right] = idx
                idx += 1
            right -= 1
            # move left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res[bottom][i] = idx
                    idx += 1
                bottom -= 1
            # move up
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res[i][left] = idx
                    idx += 1
                left += 1
        return res