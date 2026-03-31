class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        OBSTACLE = 1

        dp = [[0]*N for _ in range(M)]
        dp[0][0] = 1

        # down: 1, 0
        # right: 0, 1
        for row in range(M):
            for col in range(N):
                if obstacleGrid[row][col] == OBSTACLE:
                    continue
                
                if row-1 >= 0:
                    dp[row][col] += dp[row-1][col]
                if col-1 >= 0:
                    dp[row][col] += dp[row][col-1]


        return dp[-1][-1]