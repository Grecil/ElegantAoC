import sys

grid = [list(i.strip()) for i in sys.stdin.readlines()]
n, m = len(grid), len(grid[0])
rays = set([grid[0].index("S")])
ans = 0
for i in range(2, n, 2):
    new = []
    for j in range(m):
        if j in rays and grid[i][j] == "^":
            ans += 1
            rays.discard(j)
            new.append(j - 1)
            new.append(j + 1)
    rays.update(new)
print(ans)
