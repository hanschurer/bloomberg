# https://www.1point3acres.com/bbs/thread-1148287-1-1.html

# 题目是用一个2d character array来当沙漠，其中有一个element “c” 来当作车 和一个element “o” 来当作绿洲。求从车到绿洲的最短步数。你写代码就行、不用执行代码

# Follow up 1: 如果我们车只有一定量的油、每过一格会消耗一个unit的油、你会怎么改变你的algorithm

# Follow up 2: 如果任何一个空格是有一定量的油的加油站的话、你会怎么改变你的algorithm

'''
grid = [
    ["c","x","x"],
    ["x","x","x"],
    ["x","x","o"]
]


'''
from collections import deque


def shorted_path(grid: list[list[str]]) ->int:
    start_x, start_y, end_x, end_y = 0, 0, len(grid[0]) - 1, len(grid) - 1
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'c':
                start_x, start_y = i, j
            elif grid[i][j] == 'o':
                end_x, end_y = i, j

    q = deque([(start_x, start_y)])  # (x, y)
    visited = {(start_x, start_y)}
    step = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if r == end_x and c == end_y:
                return step
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))
        step += 1
    return -1


'''
gas = 5, each move cost 1 gas
'''
def shorted_path_followup1(grid: list[list[str]], gas: int) ->int:
    start_x, start_y, end_x, end_y = 0, 0, len(grid[0]) - 1, len(grid) - 1
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'c':
                start_x, start_y = i, j
            elif grid[i][j] == 'o':
                end_x, end_y = i, j

    q = deque([(start_x, start_y, gas)])  # (x, y, gas left)
    visited = {(start_x, start_y, gas)}
    step = 0
    while q:
        for _ in range(len(q)):
            r, c, g = q.popleft()
            if r == end_x and c == end_y:
                return step
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and g >= 1 and (nr, nc) not in visited:
                    visited.add((nr, nc, g - 1))
                    q.append((nr, nc, g - 1))
        step += 1
    return -1


'''
gas = 5, each move cost 1 gas
any cell can be a gas station that refills your gas to full
'''
def shorted_path_followup2(grid: list[list[str]], gas: int) ->int:
    start_x, start_y, end_x, end_y = 0, 0, len(grid[0]) - 1, len(grid) - 1
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'c':
                start_x, start_y = i, j
            elif grid[i][j] == 'o':
                end_x, end_y = i, j

    q = deque([(start_x, start_y, gas)])  # (x, y, gas left)
    visited = {(start_x, start_y, gas)}
    step = 0
    while q:
        for _ in range(len(q)):
            r, c, g = q.popleft()
            if r == end_x and c == end_y:
                return step
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and g >= 1 and (nr, nc) not in visited:
                    ng = g - 1
                    if grid[nr][nc] == 'g':  # gas station
                        ng = gas
                    visited.add((nr, nc, ng))
                    q.append((nr, nc, ng))
        step += 1
    return -1


print("Original test cases:")
grid = [
    ["c","x","x"],
    ["x","x","x"],
    ["x","x","o"]
]
print(shorted_path(grid))  # 4


print("Follow up 1 test cases:")
grid = [
    ["c","x","x"],
    ["x","x","x"],
    ["x","x","o"]
]
gas = 5
print(shorted_path_followup1(grid, gas))  # 4

grid = [
    ["c","x","x"],
    ["x","x","x"],
    ["x","x","o"]
]
gas = 2
print(shorted_path_followup1(grid, gas))  # -1

print("Follow up 2 test cases:")
grid = [
    ["c","x","x"],
    ["x","g","x"],
    ["x","x","o"]
]
gas = 5
print(shorted_path_followup2(grid, gas))  # 4

grid = [
    ["c","x","x"],
    ["x","g","x"],
    ["x","x","o"]
]
gas = 2
print(shorted_path_followup2(grid, gas))  # 4

