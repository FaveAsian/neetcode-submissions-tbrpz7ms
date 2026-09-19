class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        cardinal = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j):
            if (i, j) in visited:
                return
            if min(i, j) < 0 or i >= ROW or j >= COL:
                return
            if grid[i][j] == "0":
                return
            # print("here")
            visited.add((i,j))
            for row, col in cardinal:
                dfs(row+i, col+j)

        res = 0
        for i in range(ROW):
            for j in range(COL):
                print(grid[i][j], (i, j), (i, j) not in visited)
                if (grid[i][j] == "1") and ((i, j) not in visited):
                    dfs(i, j)
                    res += 1
        
        return res