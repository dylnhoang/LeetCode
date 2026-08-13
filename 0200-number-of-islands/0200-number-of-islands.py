class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        seen = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and (r, c) not in seen and grid[r][c] == "1":
                        q.append((r, c))
                        seen.add((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    islands += 1
        
        return islands

