from collections import deque
from typing import List


# DFS Solution
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


# BFS Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = 0  # mark as visited
                    neighbors = []
                    neighbors.append((r, c))
                    while neighbors:
                        row, col = neighbors.pop(0)
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = "0"
                        if row + 1 < nr and grid[row + 1][col] == "1":
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = "0"
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = "0"
                        if col + 1 < nc and grid[row][col + 1] == "1":
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = "0"
        return num_islands

    '''
    Optimized with BFS
    TC: O(m * n)
    SC: min(m, n)
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        ans, m, n = 0, len(grid), len(grid[0])

        def bfs(row: int, col: int) -> None:
            q = deque([(row, col)])
            while q:
                x, y = q.popleft()
                for nr, nc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

        for row, cols in enumerate(grid):
            for col, val in enumerate(cols):
                if val == '1':
                    grid[row][col] = '0'
                    bfs(row, col)
                    ans += 1
        return ans
