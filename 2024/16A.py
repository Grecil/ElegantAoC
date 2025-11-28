import sys
from collections import defaultdict, deque

grid = sys.stdin.read().splitlines()
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            sx, sy = i, j
        if grid[i][j] == "E":
            ex, ey = i, j
vis = defaultdict(lambda: float("inf"))
q = deque([(sx, sy, 0, 1, 0)])
while q:
    x, y, dx, dy, score = q.popleft()
    vis[(x, y, dx, dy)] = score
    if (x, y) == (ex, ey):
        continue
    if grid[x + dx][y + dy] != "#" and vis[(x + dx, y + dy, dx, dy)] > score:
        q.append((x + dx, y + dy, dx, dy, score + 1))
    if vis[(x, y, dy, -dx)] > score + 1000:
        q.append((x, y, dy, -dx, score + 1000))
    if vis[(x, y, -dy, dx)] > score + 1000:
        q.append((x, y, -dy, dx, score + 1000))
print(min(vis[(ex, ey, dx, dy)] for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1))))
