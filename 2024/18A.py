import sys
from collections import deque

arr = [list(map(int, i.split(","))) for i in sys.stdin.read().splitlines()]
grid = [[1] * 71 for _ in range(71)]
for i, j in arr[:1024]:
    grid[i][j] = 0
q = deque([(0, 0, 0)])
vis = [[False] * 71 for _ in range(71)]
while q:
    x, y, dist = q.popleft()
    vis[x][y] = True
    if (x, y) == (70, 70):
        print(dist)
        break
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if -1 < nx < 71 and -1 < ny < 71 and grid[nx][ny] == 1 and not vis[nx][ny]:
            vis[nx][ny] = True
            q.append((nx, ny, dist + 1))
