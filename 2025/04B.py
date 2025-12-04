# For Dense Grids
import sys

grid = [list(i.strip()) for i in sys.stdin.readlines()]
n, m = len(grid), len(grid[0])
for i in range(n):
    grid[i].append(".")
grid.append(["."] * (m + 1))
ans = 0
while True:
    cur = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                c = 0
                for di in (0, 1, -1):
                    for dj in (0, 1, -1):
                        c += grid[i + di][j + dj] == "@"
                if c <= 4:
                    cur += 1
                    grid[i][j] = "."
    if cur == 0:
        break
    ans += cur
print(ans)

# For Sparse Grids
import sys

grid = [i.strip() for i in sys.stdin.readlines()]
n, m = len(grid), len(grid[0])
rolls = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            rolls.add((i, j))
ans = 0
while True:
    to_rem = set()
    for roll in rolls:
        c = 0
        for i in (0, 1, -1):
            for j in (0, 1, -1):
                c += (roll[0] + i, roll[1] + j) in rolls
        if c <= 4:
            to_rem.add(roll)
    if to_rem:
        ans += len(to_rem)
        rolls -= to_rem
    else:
        break
print(ans)
