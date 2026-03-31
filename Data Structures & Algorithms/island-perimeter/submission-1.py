class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        # find first land piece
        def find_first_land(grid):
            for i in range(ROW):
                for j in range(COL):
                    if grid[i][j] == 1:
                        return i, j

        def dfs(row, col):
            if min(row, col) < 0 or row >= ROW or col >= COL:
                return 1
            
            if grid[row][col] == 0:
                return 1

            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            perimeter = 0
            for rx, cx in direction:
                perimeter += dfs(row+rx, col+cx)
            
            return perimeter
        i, j = find_first_land(grid)
        return dfs(i, j)
