class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # idea is to use dfs and mark land as visited (part of an island) as you get to new land    
        # O(N^2)

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        def dfs(r, c): # DFS algo
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0" or (r, c) in visited: # base cases
                return
            visited.add((r, c)) # mark land as visited
            
            for dr, dc in directions:
                dfs(r + dr, c + dc) # recursively check neighboring islands
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c) # mark neighboring land as part of same island
                    islands += 1
        
        return islands
