# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(x, y, start):
            if x not in range(m) or y not in range(n):
                return False
            
            if board[x][y] != word[start]:
                return False
            
            if start == len(word) - 1:
                return True
            
            visited.add((x, y))

            for nx, ny in directions:
                row = x + nx
                col = y + ny
                if (row, col) not in visited:
                    if dfs(row, col, start + 1):
                        return True
            
            visited.remove((x, y))
        
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


            

            
            
        