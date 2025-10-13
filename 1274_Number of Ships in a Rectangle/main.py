class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        def dfs(x1, y1, x2, y2):
            if (x1, y1) == (x2, y2):
                return 1 if sea.hasShips(Point(x2, y2), Point(x1, y1)) else 0
                
            if x1 > x2 or y1 > y2 or not sea.hasShips(Point(x2, y2), Point(x1, y1)):
                return 0
            x0, y0 = (x1 + x2) // 2, (y1 + y2) // 2
            ans = dfs(x1, y1, x0, y0) +dfs(x1, y0 + 1, x0, y2) + dfs(x0 + 1, y0 + 1, x2, y2) +  dfs(x0 + 1, y1, x2, y0)

            return ans

        return dfs(bottomLeft.x, bottomLeft.y, topRight.x, topRight.y)
