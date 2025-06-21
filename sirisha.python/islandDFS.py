class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != '0':
                return
            grid[r][c] = '0'  # Mark as visited
            dfs(r-1, c)  
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands       
            