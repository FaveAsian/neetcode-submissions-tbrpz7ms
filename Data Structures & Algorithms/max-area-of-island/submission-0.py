class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col) -> int:
            if min(col, row) < 0 or col >= COL or row >= ROW:
                return 0
            
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            area = 0
            cardinal = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for rx, cx in cardinal:
                area += dfs(row+rx, col+cx)
            
            return 1 + area        

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    continue
                if grid[i][j] == 1 and (i, j) in visited:
                    continue

                island_area = dfs(i, j)
                res = max(island_area, res)

        return res