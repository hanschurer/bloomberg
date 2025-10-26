class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:  
            return []  

        m, n = len(mat), len(mat[0])   # m: row, n: col
        result = []  
        total_diagonals = m + n - 1  

        '''
        elements in each diagonal has the same s = r+c, 
        if r+c even: going upper right
               odd: going lower left
        '''
        for s in range(total_diagonals):  
            '''
            start row r does not always start with 0, b/c sum s can be > m, this would make the corresponding column c out of range
            for columns to be valid: 0 <= c = s-r <= n-1
            for rows to be valid: 0 ≤ r ≤ m-1.
            combine these, we solve the start row: r ≥ max(0, s - (n - 1))
            '''
            start_row = 0 if s < n else s - (n - 1)  
            end_row = min(s, m - 1)  # last feasible row within matrix rows
            temp = []  # temporary collector for current diagonal

            for r in range(start_row, end_row + 1): 
                c = s - r  
                temp.append(mat[r][c])  

            if s % 2 == 0:  # even s means this diagonal should go up-right, reverse to get the up-right order
                temp.reverse()  

            result.extend(temp) 

        return result 

# TC: O(mn) — each cell is visited exactly once
# SC: can be O(1) if dont use temp, O(min(m,n)) 