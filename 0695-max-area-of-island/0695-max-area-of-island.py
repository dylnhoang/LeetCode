class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 0

            grid[r][c] = 0 

            res = 1

            for dr, dc in dirs:
                res += dfs(r + dr, c + dc)

            return res


        maxArea = 0
        for m in range(ROWS):
            for n in range(COLS):
                candArea = dfs(m, n)
                maxArea = max(candArea, maxArea)

        return maxArea