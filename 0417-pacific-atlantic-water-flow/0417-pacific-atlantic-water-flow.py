class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #graph dfs

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r, c))
            curHeight = heights[r][c]
            dfs(r + 1, c, visited, curHeight)
            dfs(r - 1, c, visited, curHeight)
            dfs(r, c + 1, visited, curHeight)
            dfs(r, c - 1, visited, curHeight)


        #left and right
        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        #top and bottom
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        #check if each grid in matrix is in both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
