class NumMatrix:
    '''
    1-D rule: tree[i] = last lowbit(i) elements.
        update: i += lowbit(i) ; prefix: i -= lowbit(i).

    2-D rule: bit[i][j] = rectangle with height lowbit(i) × width lowbit(j) ending at (i,j).
        update: nested i += lowbit(i) / j += lowbit(j).
        prefix: nested subtractions.

    In 1-D we do ≤ log₂ n updates/reads per operation.
    In 2-D the nested loops each run ≤ log₂ m and log₂ n, so cost becomes O(log m · log n).
    '''


    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0]) if matrix else 0
        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]   # 1-based BIT
        self.arr = [[0]*self.n for _ in range(self.m)]        
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])                  
        
    # ---------- internal helpers ----------
    def _bit_add(self, r, c, delta):              # add delta at (r,c)
        i = r+1     # 1-based row for BIT
        while i <= self.m:
            j = c+1  # 1-based col
            while j <= self.n:
                self.bit[i][j] += delta # modified affected BITblock
                j += j & -j  # next col BIT block affecrted by this change
            i += i & -i  # next row BIT block affected

    def _bit_prefixsum(self, r, c):  # prefix sum for (0,0) .. (r,c)
        if r < 0 or c < 0: 
            return 0              
        s = 0
        i = r+1
        while i:
            j = c+1
            while j:
                s += self.bit[i][j]  # accumulate block sum
                j -= j & -j   # move left in BIT
            i -= i & -i  # move up
        return s

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.arr[row][col]   # compute difference
        self.arr[row][col] = val    # store new value into the original arr
        self._bit_add(row, col, delta) # propagate delta to update BIT      

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return ( self._bit_prefixsum(row2, col2)
               - self._bit_prefixsum(row1-1, col2)
               - self._bit_prefixsum(row2, col1-1)
               + self._bit_prefixsum(row1-1, col1-1) )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)