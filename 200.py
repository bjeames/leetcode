class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            # out of bounds, water, already in visited
            if (
                r < 0 or r >= n_rows or
                c < 0 or c >= n_cols or
                grid[r][c] == '0' or
                (r,c) in visited
            ): return 
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        
        return islands



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        counter = 0

        def dfs(r,c):
            if (
                min(r,c) < 0 or
                r >= rows or c >= cols or
                (r,c) in seen or
                grid[r][c] == '0'
                ): return
            else:
                seen.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c)
                    counter +=1
        return counter

