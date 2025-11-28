import sys
from collections import deque

grid = sys.stdin.read().splitlines()
n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            sx, sy = i, j
        if grid[i][j] == "E":
            ex, ey = i, j
from_s, from_e = {}, {}
q = deque([(sx, sy, 0)])
while q:
    x, y, score = q.popleft()
    from_s[(x, y)] = score
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if -1 < x + dx < n and -1 < y + dy < m and grid[x + dx][y + dy] != "#" and (x + dx, y + dy) not in from_s:
            q.append((x + dx, y + dy, score + 1))
q = deque([(ex, ey, 0)])
while q:
    x, y, score = q.popleft()
    from_e[(x, y)] = score
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if -1 < x + dx < n and -1 < y + dy < m and grid[x + dx][y + dy] != "#" and (x + dx, y + dy) not in from_e:
            q.append((x + dx, y + dy, score + 1))
target = from_s[(ex, ey)] - 100
print(
    sum(
        start + dist + end <= target
        for (y1, x1), start in from_s.items()
        for (y2, x2), end in from_e.items()
        if (dist := abs(y2 - y1) + abs(x2 - x1)) <= 2
    )
)
