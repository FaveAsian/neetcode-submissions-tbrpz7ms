class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = [0] * len(positions)
        grid = [([0]*n) for _ in range(m)]

        for i in range(len(positions)):
            row, col = positions[i]
            grid[row][col] = 1
            num_island = self.helper(grid, m, n)
            res[i] = num_island

        return res
    
    def helper(self, grid: List[List[int]], m, n) -> int:
        visited = set()
        def dfs(row, col):
            if min(row, col) < 0 or row >= m or col >= n or (row, col) in visited or grid[row][col] == 0:
                return
            
            visited.add((row, col))
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for rx, cx in directions:
                dfs(row+rx, col+cx)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    res += 1
        return res