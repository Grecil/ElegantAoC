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
q = deque([(sx, sy, 0, 1, 0, {(sx, sy)})])
ans = set()
while q:
    x, y, dx, dy, score, path = q.popleft()
    if (x, y) == (ex, ey):
        mn = min(vis[(x, y, i, j)] for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)))
        if score == mn:
            ans |= path
        elif score < mn:
            ans = path
            vis[(x, y, dx, dy)] = score
        continue
    vis[(x, y, dx, dy)] = score
    if grid[x + dx][y + dy] != "#" and vis[(x + dx, y + dy, dx, dy)] > score:
        q.append((x + dx, y + dy, dx, dy, score + 1, path | {(x + dx, y + dy)}))
    if vis[(x, y, dy, -dx)] > score + 1000:
        q.append((x, y, dy, -dx, score + 1000, path))
    if vis[(x, y, -dy, dx)] > score + 1000:
        q.append((x, y, -dy, dx, score + 1000, path))
print(len(ans))
