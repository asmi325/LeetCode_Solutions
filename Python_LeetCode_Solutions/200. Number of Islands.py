
class Solution(object):
    def numIslands(self,grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            # Check bounds and whether the cell is unvisited land
            if (
                r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == "0" or (r, c) in visited
            ):
                return
            visited.add((r, c))
            # Visit all adjacent cells
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        islands = 0

        for r in range(rows):
            for c in range(cols):
                # If the cell is land and not visited, it's a new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands
