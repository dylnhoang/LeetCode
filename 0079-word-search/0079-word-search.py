class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word): #all chars found
                return True
            elif (r < 0 or c < 0 or c >= COLS or r >= ROWS or board[r][c] != word[i] or (r, c) in visited): #invalidate path
                return False
            
            #otherwise, necessary char found, so move to next char in word
            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)
                  )
            visited.remove((r, c)) #free to remove bc we've seen the path from here

            return res
        
        #start from every square on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False