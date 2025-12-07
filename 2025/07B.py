import sys
from collections import defaultdict

grid = [list(i.strip()) for i in sys.stdin.readlines()]
n, m = len(grid), len(grid[0])
rays = defaultdict(int)
rays[grid[0].index("S")] = 1
for i in range(2, n, 2):
    new = []
    for j in range(m):
        if j in rays and grid[i][j] == "^":
            new.append((j - 1, rays[j]))
            new.append((j + 1, rays[j]))
            del rays[j]
    for j, f in new:
        rays[j] += f
print(sum(rays.values()))
