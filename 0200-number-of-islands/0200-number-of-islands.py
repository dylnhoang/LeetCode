class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0" or (r, c) in seen:
                return
            else:
                seen.add((r, c))
                for dr, dc in dirs:
                    dfs(r + dr, c + dc)
                
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
        
        return islands
        


                    
