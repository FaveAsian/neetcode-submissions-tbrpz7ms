class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        cardinal = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if min(i, j) < 0 or i >= ROW or j >= COL:
                return
            if grid[i][j] == "-1" or grid[i][j] == "0":
                return
            grid[i][j] = "-1"
            for row, col in cardinal:
                dfs(row+i, col+j)

        res = 0
        for i in range(ROW):
            for j in range(COL):
                if (grid[i][j] == "1"):
                    dfs(i, j)
                    res += 1
        return res