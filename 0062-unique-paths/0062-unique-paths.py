class Solution(object):
    def uniquePaths(self, m, n):
        # idea: since you can only move right and down at any point, the ways you can get to a point (x, y) is either from (x - 1, y) or (x, y + 1)
        # because of this, we can apply DP to this problem, stating that the amount of paths to (x, y) is the sum of the amount of paths to (x - 1, y) and the amount of paths to (x, y + 1)
        # base case: the grids on the leftmost column and uppermost row only have one path towards them (which is starting there)

        dp = [[1 for _ in range(n)] for _ in range(m)] # 2D grid: dp[m][n] is the number of paths you can use to get to grid[m][n]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
        