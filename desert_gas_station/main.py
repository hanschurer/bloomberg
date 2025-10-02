# 题目是用一个2d character array来当沙漠，其中有一个element “c” 来当作车 和一个element “o” 来当作绿洲。求从车到绿洲的最短步数。你写代码就行、不用执行代码

# Follow up 1: 如果我们车只有一定量的油、每过一格会消耗一个unit的油、你会怎么改变你的algorithm

# Follow up 2: 如果任何一个空格是有一定量的油的加油站的话、你会怎么改变你的algorithm


def shorted_path(grid: list[list[str]]) ->int:

    m, n = len(gird), len(grid[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    def bfs(r,c):


    for r in range(m):
        for c in range(n):
            if gird[r][c] == "c":
                start = (r,c)
            if gird[r][c] == "0":
                destination = (r,c)
    
    def bfs(r,c):
        q = [(r,c)]

        while q:
            r,c,step = q.popleft()

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if nr in range(m) and nc in range(n) and 


    res = min(res, bfs(start[0], start[1]))
        
    return step